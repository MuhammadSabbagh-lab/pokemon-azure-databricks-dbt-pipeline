-- dbt Bronze model
-- Reads the curated Databricks Gold engineering table into the dbt layer.

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
    total_base_stat,
    base_experience,
    height_metres,
    weight_kg,
    sprite_url
FROM databricks_learning_premium.default.gold_pokemon_dashboard
