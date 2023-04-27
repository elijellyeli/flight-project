{{ 
    config(
        materialized='table',
        unique_key="flight_id",
        partition_by={
            "field": "first_seen",
            "data_type": "timestamp",
            "granularity": "day",
        },
        cluster_by=["flight_type", "dep_airport", "arr_airport"]
    ) 
}}

with
    arrivals as (select * from {{ ref("stg_arrivals") }}),
    departures as (select * from {{ ref("stg_departures") }}),
    flights_unioned as (
                select *
                from arrivals
                union all
                select *
                from departures
            ),
    airlines as (select * from {{ ref("stg_airlines") }}),
    airports as (select * from {{ ref("stg_airports") }}),
    final as (
        select 
            fu.*,
            al.name as airline_name, 
            al.iata as airline_aita, 
            al.icao as airline_icao, 
            al.country as airline_country, 
            dap.name as dep_airport_name,
            dap.city as dep_airport_city,
            dap.country as dep_airport_country,
            aap.name as arr_airport_name,
            aap.city as arr_airport_city,
            aap.country as arr_airport_country
        from flights_unioned fu 
        left join airlines al on LEFT(fu.callsign,3) = al.icao
        left join airports dap on fu.dep_airport = dap.icao 
        left join airports aap on fu.arr_airport = aap.icao 
    )

select * from final
