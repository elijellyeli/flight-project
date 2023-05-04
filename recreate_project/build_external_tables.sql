CREATE OR REPLACE EXTERNAL TABLE `flights-project-383517.raw.external_arrival`
    (icao24 STRING,
    first_seen TIMESTAMP,
    dep_airport STRING,
    last_seen TIMESTAMP,
    arr_airport STRING,
    callsign STRING,
    dep_airport_horiz_distance INT64,
    dep_airport_vert_distance INT64,
    arr_airport_horiz_distance INT64,
    arr_airport_vert_distance INT64)
OPTIONS (
  format = 'PARQUET',
  uris = [
    'gs://flights_project_120423/data/arrivals/arrivals_LLBG_*.parquet'
  ]
);




CREATE OR REPLACE EXTERNAL TABLE `flights-project-383517.raw.external_departure`
    (icao24 STRING,
    first_seen TIMESTAMP,
    dep_airport STRING,
    last_seen TIMESTAMP,
    arr_airport STRING,
    callsign STRING,
    dep_airport_horiz_distance INT64,
    dep_airport_vert_distance INT64,
    arr_airport_horiz_distance INT64,
    arr_airport_vert_distance INT64)
OPTIONS (
  format = 'PARQUET',
  uris = [
    'gs://flights_project_120423/data/departures/departures_LLBG_*.parquet'
  ]
);


CREATE OR REPLACE EXTERNAL TABLE `flights-project-383517.raw.airports`
    (airport_id INT64,
    name STRING,
    city STRING,
    country STRING,
    iata STRING,
    icao STRING,
    lat FLOAT64,
    long FLOAT64,
    altitue_feet INT64,
    timezone FLOAT64,
    dst STRING,
    tz STRING,
    type STRING,
    src STRING)
OPTIONS (
  format = 'CSV',
  null_marker = '\\N',
  uris = [
    'gs://flights_project_120423/data/seed/airports.csv'
  ]
);


CREATE OR REPLACE EXTERNAL TABLE `flights-project-383517.raw.airports`
    (airport_id INT64,
    name STRING,
    city STRING,
    country STRING,
    iata STRING,
    icao STRING,
    lat FLOAT64,
    long FLOAT64,
    altitue_feet INT64,
    timezone FLOAT64,
    dst STRING,
    tz STRING,
    type STRING,
    src STRING)
OPTIONS (
  format = 'CSV',
  null_marker = '\\N',
  uris = [
    'gs://flights_project_120423/data/seed/airports.csv'
  ]
);
