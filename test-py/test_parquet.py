""" For reading a Parquet File """
import pyarrow.parquet as pq

def clean() -> None:
    """"Fix parquet file datatypes"""
    src_file = 'data/data_arrival_arrivals_LLBG_2023_03_30.parquet'
    table = pq.read_table(src_file)
    print(table)
    
    
if __name__ == "__main__":
    clean()