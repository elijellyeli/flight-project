from os import path
import json
from datetime import datetime, timedelta, timezone
import pandas as pd
from pandas import DataFrame
from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from mage_ai.data_preparation.variable_manager import get_variable



if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df, *args, **kwargs) -> None:
    """
    export to gcs bucket
    """

    print(f'args={args}')
    print(f'kwargs={kwargs}')

    dt = kwargs['execution_date']
    print(f'execution date={dt}')
    dt_end = datetime(
                    dt.year, dt.month, dt.day, 
                    23, 59, 59, tzinfo = timezone.utc )
    yesterday_end = dt_end - timedelta(days=1)
    yesterday_beginning = yesterday_end.replace(hour=0, minute=0, second=0)
    # extract timestamp
    start_ts = int(yesterday_beginning.timestamp())

    print(f'start_ts={start_ts}')
    print(f'df len={len(df)}')
    # TODO Change to env variable bla
    bucket_name = 'flights_project_120423'

    # get output from first step
    airport = kwargs['airport']

    start_str = datetime.utcfromtimestamp(start_ts).strftime('%Y_%m_%d')
    
    print(f'start_time={start_ts}')
    print(f'start_str={start_str}')

    file_name = f'arrivals_{airport}_{start_str}.parquet'
    obj_key = f'data/arrival/{file_name}'

    print(f'obj_key={obj_key}')
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    GoogleCloudStorage() \
        .with_config(ConfigFileLoader(config_path, config_profile)) \
        .export(
            df=df,
            bucket_name=bucket_name,
            object_key=obj_key,
            format='parquet'
        )