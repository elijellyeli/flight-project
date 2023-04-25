import pyarrow as pa
import pyarrow.parquet as pq

# from prefect import flow, task
# from prefect_gcp.cloud_storage import GcsBucket

# table_schema_green = pa.schema(
#     [
#         ('VendorID',pa.string()),
#         ('lpep_pickup_datetime',pa.timestamp('s')),
#         ('lpep_dropoff_datetime',pa.timestamp('s')),
#         ('store_and_fwd_flag',pa.string()),
#         ('RatecodeID',pa.int64()),
#         ('PULocationID',pa.int64()),
#         ('DOLocationID',pa.int64()),
#         ('passenger_count',pa.int64()),
#         ('trip_distance',pa.float64()),
#         ('fare_amount',pa.float64()),
#         ('extra',pa.float64()),
#         ('mta_tax',pa.float64()),
#         ('tip_amount',pa.float64()),
#         ('tolls_amount',pa.float64()),
#         ('ehail_fee',pa.float64()),
#         ('improvement_surcharge',pa.float64()),
#         ('total_amount',pa.float64()),
#         ('payment_type',pa.int64()),
#         ('trip_type',pa.int64()),
#         ('congestion_surcharge',pa.float64()),
#     ]
# )

# table_schema_yellow = pa.schema(
#    [
#         ('VendorID', pa.string()), 
#         ('tpep_pickup_datetime', pa.timestamp('s')), 
#         ('tpep_dropoff_datetime', pa.timestamp('s')), 
#         ('passenger_count', pa.int64()), 
#         ('trip_distance', pa.float64()), 
#         ('RatecodeID', pa.string()), 
#         ('store_and_fwd_flag', pa.string()), 
#         ('PULocationID', pa.int64()), 
#         ('DOLocationID', pa.int64()), 
#         ('payment_type', pa.int64()), 
#         ('fare_amount',pa.float64()), 
#         ('extra',pa.float64()), 
#         ('mta_tax', pa.float64()), 
#         ('tip_amount', pa.float64()), 
#         ('tolls_amount', pa.float64()), 
#         ('improvement_surcharge', pa.float64()), 
#         ('total_amount', pa.float64()), 
#         ('congestion_surcharge', pa.float64())]

# )


def clean() -> None:
    """"Fix parquet file datatypes"""
    src_file = 'data/data_arrival_arrivals_LLBG_2023_03_30.parquet'
    table = pq.read_table(src_file)
    print(table)
    
    
if __name__ == "__main__":
    clean()