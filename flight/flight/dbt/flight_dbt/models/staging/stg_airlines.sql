{{ 
    config(
        materialized='table',
        unique_key="airline_id"
    ) 
}}


with d as (
    select
        airline_id,
        name,
        alias,
        {{ replace_empty_string_null('iata') }},
        icao,
        {{ replace_empty_string_null('callsign') }},
        country
        ROW_NUMBER() OVER (PARTITION BY icao ORDER BY airline_id desc) as row_number
    from {{ source('raw','airlines')}}
    where active = 'Y'
),
--  Get Rid of double airlines - with the same ICAO
final as (
    select
        *
    from d
    where row_number = 1
)
  

select * from final