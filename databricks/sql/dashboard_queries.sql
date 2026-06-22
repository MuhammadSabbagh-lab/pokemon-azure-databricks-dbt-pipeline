-- Databricks SQL dashboard queries
-- These queries were used to build the final Pokémon dashboard visualisations.

-- 1. Pokémon count by primary type

SELECT
    primary_type,
    pokemon_count
FROM databricks_learning_premium.dbt_mo.gold_pokemon_type_dashboard
ORDER BY pokemon_count DESC;


-- 2. Average total base stat by primary type

SELECT
    primary_type,
    avg_total_base_stat
FROM databricks_learning_premium.dbt_mo.gold_pokemon_type_dashboard
ORDER BY avg_total_base_stat DESC;


-- 3. Average attack by primary type

SELECT
    primary_type,
    avg_attack
FROM databricks_learning_premium.dbt_mo.gold_pokemon_type_dashboard
ORDER BY avg_attack DESC;


-- 4. Average speed by primary type

SELECT
    primary_type,
    avg_speed
FROM databricks_learning_premium.dbt_mo.gold_pokemon_type_dashboard
ORDER BY avg_speed DESC;


-- 5. Full final dashboard table

SELECT *
FROM databricks_learning_premium.dbt_mo.gold_pokemon_type_dashboard
ORDER BY pokemon_count DESC;
