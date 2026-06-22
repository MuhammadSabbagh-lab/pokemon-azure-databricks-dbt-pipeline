-- dbt Silver model
-- Aggregates Pokémon statistics by primary type.

SELECT
    primary_type,
    COUNT(*) AS pokemon_count,
    ROUND(AVG(total_base_stat), 2) AS avg_total_base_stat,
    ROUND(AVG(hp), 2) AS avg_hp,
    ROUND(AVG(attack), 2) AS avg_attack,
    ROUND(AVG(defense), 2) AS avg_defense,
    ROUND(AVG(special_attack), 2) AS avg_special_attack,
    ROUND(AVG(special_defense), 2) AS avg_special_defense,
    ROUND(AVG(speed), 2) AS avg_speed,
    ROUND(AVG(height_metres), 2) AS avg_height_metres,
    ROUND(AVG(weight_kg), 2) AS avg_weight_kg
FROM {{ ref('bronze_pokemon') }}
GROUP BY primary_type
