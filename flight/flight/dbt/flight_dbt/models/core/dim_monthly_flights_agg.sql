{{ config(materialized="view") }}

with flight_data as (select * from {{ ref("fact_flights") }})

select
    -- grouping 
    flight_type,
    dep_airport,
    arr_airport,
    date_trunc(first_seen, month) as agg_date,
    -- Agg Functions
    count(flight_id) as cnt_flights,
    count(distinct icao24) as cnt_distinct_icao24,
    count(distinct airline_name) as cnt_airlines
    
from flight_data
group by 1, 2, 3, 4
