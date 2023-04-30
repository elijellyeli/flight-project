# flight-project

Final project for the Data Engineer Zoomcamp Course


## Used Sources

1. https://opensky-network.org/api
2. Airport, Airline Files from https://openflights.org/data.html


#### Project Framing

It uses the Open Sky API to retrive arrival & departure flights out of a given airport (in my case LLBG - Ben Gurion Airport in Israel), and cross refrences it with data from OpenFlights such as Airports & Airlines for extra information.

#### Steps

This project is meant to demonstrate the flow of data from raw to dashboard:

* Extracting the data from the API & raw files, in an orchestration tool (in this case i've used Mage) in an automated manner
* Ingest the data by loading the transformed parquet files into a GCS bucket,
* Load into a DWH & Transform the data using DBT - creating staging & core models
* Connect the final models into a BI Dashboard, and investigate the data to extract insights!
