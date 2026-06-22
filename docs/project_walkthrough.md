# Project Walkthrough

## Project Goal

The goal of this project was to build an end-to-end cloud data engineering pipeline using Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, dbt and Databricks dashboards.

The pipeline ingests Pokémon data from the PokéAPI, stores the raw data in ADLS Gen2, transforms it using Databricks, models it further using dbt, and visualises the final output in Databricks dashboards.

---

## Step 1: API Ingestion with Azure Data Factory

Azure Data Factory was used to call the PokéAPI and ingest Pokémon data.

The ingestion process used:

- A Web activity to call the PokéAPI
- A ForEach activity to loop through Pokémon records
- A Copy activity to write raw JSON files into Azure Data Lake Storage Gen2

The raw data was landed in ADLS under a path similar to:

```text
raw/pokeapi/pokemon_details/
