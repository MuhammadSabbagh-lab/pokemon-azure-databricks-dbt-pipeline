# Project Walkthrough

## Project Goal

The goal of this project was to build an end-to-end cloud data engineering pipeline using Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, dbt and Databricks dashboards.

The pipeline ingests Pokémon data from the PokéAPI, stores the raw data in ADLS Gen2, transforms it using Databricks, models it further using dbt, and visualises the final output in Databricks dashboards.

---

## Step 1: API Ingestion with Azure Data Factory

Azure Data Factory was used to call the PokéAPI and ingest Pokémon data.

The ingestion process used:

* A Web activity to call the PokéAPI
* A ForEach activity to loop through Pokémon records
* A Copy activity to write raw JSON files into Azure Data Lake Storage Gen2

The raw data was landed in ADLS under a path similar to:

```text
raw/pokeapi/pokemon_details/
```

---

## Step 2: Raw Landing Zone in ADLS Gen2

Azure Data Lake Storage Gen2 acted as the raw landing zone.

This means the original Pokémon API data was stored before any transformations were applied.

This gives the pipeline traceability because the raw source data can be reprocessed if needed.

---

## Step 3: Databricks Bronze Layer

Databricks read the raw JSON files from ADLS.

The Bronze table stored the raw structured Pokémon data from the API.

The Bronze layer preserved useful metadata, including the source file path. This allowed the pipeline to track where each record came from.

---

## Step 4: Databricks Silver Layer

The Silver layer cleaned and standardised the Pokémon data.

This included extracting useful fields such as:

* Pokémon ID
* Pokémon name
* Primary type
* Secondary type
* Abilities
* HP
* Attack
* Defence
* Special attack
* Special defence
* Speed
* Total base stat
* Height
* Weight
* Sprite URL

Nested API fields were flattened into a cleaner table structure.

---

## Step 5: Databricks Gold Layer

The Gold layer created a dashboard-ready Pokémon dataset.

This table was used as the curated output from the Databricks engineering process.

The Gold layer made the data easier to query, model and visualise.

---

## Step 6: dbt Analytics Modelling

dbt was used on top of the Databricks outputs to create analytics models.

The dbt models included:

| Model                         | Description                                    |
| ----------------------------- | ---------------------------------------------- |
| `bronze_pokemon`              | Reads curated Databricks Pokémon data into dbt |
| `silver_pokemon_type_stats`   | Aggregates Pokémon statistics by primary type  |
| `gold_pokemon_type_dashboard` | Final dashboard-ready dbt model                |

dbt was also used to define model documentation and data tests.

---

## Step 7: Databricks Dashboard

The final dbt gold model was visualised using Databricks SQL dashboards.

The dashboard included:

* Pokémon count by primary type
* Average total base stat by primary type
* Average attack by primary type
* Average speed by primary type
* Final gold dashboard table

---

## Step 8: Orchestration

The pipeline was designed so that the ingestion, Databricks transformations and dbt models could be run as part of an automated process.

The target flow was:

```text
ADF ingestion → Databricks Bronze/Silver/Gold → dbt models → Dashboard refresh
```

A daily trigger was added in Azure Data Factory so that the pipeline could run automatically.

---

## Outcome

This project demonstrates how to build a practical cloud data engineering pipeline using Azure, Databricks and dbt.

It shows experience with:

* API ingestion
* Cloud data lake storage
* Medallion architecture
* PySpark transformations
* SQL modelling
* dbt tests and documentation
* Dashboarding
* Pipeline orchestration
