{{ 
    config(
        materialized='table',
        unique_key="route_id"
    ) 
}}
with d as (
    select
        {{ dbt_utils.generate_surrogate_key(['airline_id', 'src_airport', 'dst_airport']) }} as route_id,
        airline_code,
        airline_id,
        src_airport,
        src_airport_id,
        dst_airport,
        dst_airport_id,
        codeshare, 
        stops
    from {{ source('raw','routes')}}
    where src_airport = 'TLV' or dst_airport = 'TLV'
)

select * from d