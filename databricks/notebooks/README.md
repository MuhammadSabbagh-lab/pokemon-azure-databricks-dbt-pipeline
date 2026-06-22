# Databricks Notebooks

This folder contains exported Databricks notebooks used for the Pokémon medallion pipeline.

Expected notebooks:

| Notebook | Purpose |
|---|---|
| `01_bronze_pokemon_details.py` | Reads raw Pokémon JSON files from ADLS and creates the Bronze table |
| `02_silver_pokemon.py` | Cleans and standardises the Bronze Pokémon data |
| `03_gold_pokemon_dashboard.py` | Creates the final Gold engineering table used for analytics |

The notebooks were developed in Azure Databricks and exported as source files for version control.
