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
        case 
            when iata = '' then null
            else iata
        end as iata,
        icao,
        case 
            when callsign = '' then null
            else callsign
        end as callsign,
        country
    from {{ source('raw','airlines')}}
    where active = 'Y'
)

select * from d