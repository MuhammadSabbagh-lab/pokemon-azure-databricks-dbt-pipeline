# Azure Data Factory Pipeline Overview

Azure Data Factory was used to orchestrate the ingestion of Pokémon data from the PokéAPI into Azure Data Lake Storage Gen2.

Main pipeline stages:

1. Call the PokéAPI.
2. Retrieve Pokémon detail JSON data.
3. Write the raw JSON files into ADLS Gen2.
4. Trigger Databricks processing.
5. Trigger dbt models.
