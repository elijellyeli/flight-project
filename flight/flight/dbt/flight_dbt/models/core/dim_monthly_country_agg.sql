{{ config(materialized="view") }}

with flight_data as (select * from {{ ref("fact_flights") }})

select
    -- grouping 
    flight_type,
    date_trunc(first_seen, month) as agg_date,
    -- Agg Functions
    count(flight_id) as cnt_flights,
    count(distinct icao24) as cnt_distinct_icao24,
    count(distinct airline_name) as cnt_airlines,
    count(distinct dep_airport_country) as cnt_dep_country,
    count(distinct arr_airport_country) as cnt_arr_country,
    sum(est_flight_length_min) as sum_flight_minutes,
    avg(est_flight_length_min) as avg_flight_minutes
    
from flight_data
group by 1, 2
