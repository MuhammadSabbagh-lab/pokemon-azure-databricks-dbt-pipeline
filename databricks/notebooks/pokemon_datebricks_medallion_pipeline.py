from pyspark.sql.functions import current_timestamp, col

# =====================================
# 1. WHERE THE RAW FILES ARE
# =====================================

raw_path = "abfss://raw@stdatalakepokemon001.dfs.core.windows.net/pokeapi/pokemon_details/"

# Change this if you are using a different schema
target_schema = "default"

bronze_table = f"{target_schema}.bronze_pokemon_details"
silver_table = f"{target_schema}.silver_pokemon"
gold_table = f"{target_schema}.gold_pokemon_dashboard"


# =====================================
# 2. BUILD BRONZE TABLE
# raw JSON files → bronze table
# =====================================

bronze_df = (
    spark.read
    .option("multiLine", "true")
    .json(raw_path)
    .withColumn("ingestion_timestamp", current_timestamp())
    .withColumn("source_file", col("_metadata.file_path"))
)

bronze_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(bronze_table)

print("Bronze table built")


# =====================================
# 3. BUILD SILVER TABLE
# bronze table → cleaned Pokémon table
# =====================================

silver_df = spark.sql(f"""
SELECT
    id AS pokemon_id,
    name AS pokemon_name,

    try_element_at(
        transform(filter(types, x -> x.slot = 1), x -> x.type.name),
        1
    ) AS primary_type,

    try_element_at(
        transform(filter(types, x -> x.slot = 2), x -> x.type.name),
        1
    ) AS secondary_type,

    array_join(transform(types, x -> x.type.name), ', ') AS all_types,
    array_join(transform(abilities, x -> x.ability.name), ', ') AS abilities,

    try_element_at(transform(filter(stats, x -> x.stat.name = 'hp'), x -> x.base_stat), 1) AS hp,
    try_element_at(transform(filter(stats, x -> x.stat.name = 'attack'), x -> x.base_stat), 1) AS attack,
    try_element_at(transform(filter(stats, x -> x.stat.name = 'defense'), x -> x.base_stat), 1) AS defense,
    try_element_at(transform(filter(stats, x -> x.stat.name = 'special-attack'), x -> x.base_stat), 1) AS special_attack,
    try_element_at(transform(filter(stats, x -> x.stat.name = 'special-defense'), x -> x.base_stat), 1) AS special_defense,
    try_element_at(transform(filter(stats, x -> x.stat.name = 'speed'), x -> x.base_stat), 1) AS speed,

    base_experience,
    height / 10.0 AS height_metres,
    weight / 10.0 AS weight_kg,
    sprites.front_default AS sprite_url,

    ingestion_timestamp,
    source_file

FROM {bronze_table}
WHERE id IS NOT NULL
""")

silver_df = silver_df.dropDuplicates(["pokemon_id"])

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(silver_table)

print("Silver table built")


# =====================================
# 4. BUILD GOLD TABLE
# silver table → dashboard table
# =====================================

gold_df = spark.sql(f"""
SELECT
    pokemon_id,
    pokemon_name,
    primary_type,
    secondary_type,
    all_types,
    abilities,
    hp,
    attack,
    defense,
    special_attack,
    special_defense,
    speed,

    hp + attack + defense + special_attack + special_defense + speed AS total_base_stat,

    base_experience,
    height_metres,
    weight_kg,
    sprite_url

FROM {silver_table}
WHERE pokemon_id IS NOT NULL
""")

gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(gold_table)

print("Gold dashboard table built")


# =====================================
# 5. CHECK IT WORKED
# =====================================

display(spark.sql(f"""
SELECT *
FROM {gold_table}
ORDER BY pokemon_id
LIMIT 20
"""))

display(spark.sql(f"""
SELECT
    primary_type,
    COUNT(*) AS pokemon_count,
    ROUND(AVG(total_base_stat), 2) AS avg_total_base_stat,
    ROUND(AVG(attack), 2) AS avg_attack,
    ROUND(AVG(speed), 2) AS avg_speed
FROM {gold_table}
GROUP BY primary_type
ORDER BY pokemon_count DESC
"""))
