-- dbt Gold model
-- Final dashboard-ready model for Pokémon type analysis.

SELECT
    primary_type,
    pokemon_count,
    avg_total_base_stat,
    avg_hp,
    avg_attack,
    avg_defense,
    avg_special_attack,
    avg_special_defense,
    avg_speed,
    avg_height_metres,
    avg_weight_kg
FROM {{ ref('silver_pokemon_type_stats') }}
ORDER BY pokemon_count DESC
