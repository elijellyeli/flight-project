## Overview

This is my final project submission for the Data Engineer Zoomcamp Course. It aims to build an end-to-end orchestrated data pipeline, using technologies such as Google Cloud Platform (GCP), Docker, Python programming, DBT and more.

For my project I decided to explore arrivals & departure flight patterns, specificly from Israel's Ben Gurion Airport (airport code LLBG). I've used a free API by OpenSky Network that has the ability to query by airport and a given timeframe. Another data source I've used are airport & airline info from OpenFlights, in order to cross reference the data and get more info such as origin country, airline name, etc.

The Flight data is queried daily, saved the result in a Parquet file on Google Cloud Storage (GCS), and pulled to BigQuery Data-Warehouse. Then, with the help of DBT, models (SQL tables) are built on-top of these files - first staging models, and then core models ready for consumtion. Finally, I've created a dashboard in Power BI with two tiles in order to investigate the patterns in a graphical manner - with bar charts, maps and timelines.

## Business Questions

1. How many flights are arriving/departing from LLBG?
2. What are the top airlines that fly into/out of LLBG?
3. From which countries are the arrivals/departures coming from?
4. How long, on average, are these flights?
5. What is the difference on a monthly level of all these questions above?

## Technologies

* Container Development: `Docker`
* Cloud: `Google Cloud Platform (GCP)`
* Data Lake: `Google Cloud Storage (GCS)`
* Data Transformation: `DBT`
* Data Warehouse: `BigQuery`
* Orchestration Tool: `Mage AI`
* Data Visualization: `Power BI`
* Programing Langues: `SQL & Python`

## Architecture

## Steps

This project is meant to demonstrate the end-to-end flow of data from raw to dashboard:

* Extract the data from the API on a daily basis and the raw files as well, in an orchestration tool (Mage AI) in an automated manner.
* Ingest the API data by loading transformed parquet files into a GCS bucket.
* Load external files into a BigQuery Data Warehouse, and transform the data using DBT - creating staging & core models.
* Connect the final models (SQL tables) into a Power BI Dashboard, and investigate the data to extract insights.

https://app.powerbi.com/view?r=eyJrIjoiMTExYzNhM2EtZjExOS00NTZkLTllOGEtODNiZjE1M2QzYTE0IiwidCI6ImE3YzJiM2ZlLWE2ZjQtNDk0Ni04YjI0LTc4OTM0NmYzMjcyZCIsImMiOjl9&pageName=ReportSectionfb7b74e107e6c96c0524


## Screen Shots
