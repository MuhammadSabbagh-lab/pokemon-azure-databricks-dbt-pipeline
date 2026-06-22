# Pokémon Azure Databricks dbt Pipeline

## Project Overview

This project is an end-to-end cloud data engineering pipeline built using Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, dbt, and Databricks dashboards.

The pipeline ingests Pokémon data from the PokéAPI, lands the raw JSON files in Azure Data Lake Storage, processes the data through a Databricks medallion architecture, applies analytics modelling using dbt, and visualises the final gold model in Databricks dashboards.

The project was built to demonstrate practical data engineering skills using modern cloud tools.

## Tools Used

- Azure Data Factory: API ingestion and orchestration
- Azure Data Lake Storage Gen2: raw data landing zone
- Azure Databricks: Spark/PySpark processing and medallion architecture
- dbt: SQL modelling, testing, documentation and analytics layer
- Databricks SQL Dashboards: final reporting and visualisation layer
- GitHub: project version control and documentation

## Architecture

```text
PokéAPI
   ↓
Azure Data Factory
   ↓
Azure Data Lake Storage Gen2
   ↓
Azure Databricks
   ↓
Bronze → Silver → Gold
   ↓
dbt Models
   ↓
Databricks SQL Dashboard
