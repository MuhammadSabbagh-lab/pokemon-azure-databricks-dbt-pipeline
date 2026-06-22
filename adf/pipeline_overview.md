# Azure Data Factory Pipeline Overview

## Purpose

Azure Data Factory was used to orchestrate the ingestion and processing stages of the Pokémon data pipeline.

ADF was responsible for calling the PokéAPI, landing raw JSON files in Azure Data Lake Storage Gen2, and triggering downstream Databricks and dbt processing.

---

## Pipeline 1: Pokémon API Ingestion

Pipeline name:

`pl_ingest_pokemon_details_raw`

Purpose:

This pipeline ingests Pokémon data from the PokéAPI and stores the raw JSON files in ADLS Gen2.

Main activities:

1. Web activity calls the PokéAPI.
2. ForEach activity loops through the Pokémon records.
3. Copy activity writes each Pokémon detail response as a JSON file.
4. Files are stored in the raw ADLS container.

Raw output path:

`raw/pokeapi/pokemon_details/`

---

## Pipeline 2: Databricks Medallion Processing

Pipeline name:

`run_pokemon_bronze_silver_gold`

Purpose:

This pipeline triggers the Databricks notebook process that creates the Bronze, Silver and Gold engineering tables.

Main outputs:

- Bronze Pokémon details table
- Silver cleaned Pokémon table
- Gold dashboard-ready Pokémon table

---

## Pipeline 3: dbt Model Run

Pipeline name:

`run_pokemon_dbt_models`

Purpose:

This pipeline triggers the dbt models that sit on top of the Databricks outputs.

Main dbt models:

- `bronze_pokemon`
- `silver_pokemon_type_stats`
- `gold_pokemon_type_dashboard`

---

## End-to-End Flow

PokéAPI  
↓  
Azure Data Factory  
↓  
ADLS Gen2 raw JSON files  
↓  
Databricks Bronze/Silver/Gold tables  
↓  
dbt analytics models  
↓  
Databricks SQL dashboard  

---

## Automation

A daily trigger was added in Azure Data Factory so that the full pipeline could be run automatically.
