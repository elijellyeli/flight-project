{{ 
    config(
        materialized='table',
        unique_key="airport_id"
    ) 
}}


with d as (
    select
        airport_id,  
        name, 
        {{ replace_empty_string_null('city') }},
        country, 
        iata,
        icao, 
        lat, 
        long, 
        altitue_feet
    from {{ source('raw','airports')}}
)

select * from d