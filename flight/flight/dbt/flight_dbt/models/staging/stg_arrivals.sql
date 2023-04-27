{{ 
    config(
        materialized='table',
        unique_key="flight_id",
        partition_by={
            "field": "first_seen",
            "data_type": "timestamp",
            "granularity": "day",
        },
        cluster_by=["dep_airport", "icao24"]
    ) 
}}


with d as (
    select
        icao24,
        first_seen,
        dep_airport,
        last_seen,
        arr_airport,
        callsign,
        dep_airport_horiz_distance,
        dep_airport_vert_distance,
        arr_airport_horiz_distance,
        arr_airport_vert_distance,
        'arrival' as flight_type
    from {{ source('raw','external_arrival')}}
    -- dbt build --select stg_divvy_data.sql --var 'is_test_run: false'
    {% if var('is_test_run', default=true) %}
    limit 100
    {% endif %}
), 

final as (
    SELECT 
        {{ dbt_utils.generate_surrogate_key(['flight_type', 'first_seen', 'icao24']) }} as flight_id,
        d.*
    FROM d
)

select distinct * from final
