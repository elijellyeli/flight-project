import pandas as pd
import requests
from os import getenv
from mage_ai.data_preparation.variable_manager import get_variable
from mage_ai.data_preparation.shared.secrets import get_secret_value

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(dates, *args, **kwargs):
    """
    load arrivals from open-sky
    """

    print(f'dates={dates}')
    print(f'args={args}')
    print(f'kwargs={kwargs}')

    start_ts = dates['start']
    end_ts = dates['end']
    airport = kwargs['airport']

    url_txt = f'https://opensky-network.org/api/flights/arrival?airport={airport}&begin={start_ts}&end={end_ts}'
    auth_tpl = (
        getenv('OS_USERNAME'),
        getenv('OS_PASSWORD'))

    print(f'url_txt = {url_txt}')
    # response = requests.get(url=url_txt, timeout=120)
    response = requests.get(url=url_txt, auth=auth_tpl, timeout=120)
    response_txt = response.json()

    df_arrivals = pd.DataFrame.from_dict(response_txt)

    df_arrivals.columns = [
        'icao24', 'first_seen', 'dep_airport', 'last_seen', 'arr_airport', 'callsign',
        'dep_airport_horiz_distance', 'dep_airport_vert_distance',
        'arr_airport_horiz_distance', 'arr_airport_vert_distance',
        'dep_airport_candidates', 'dep_airport_candidates' ]
        
    df_arrivals['dep_airport_horiz_distance'] = df_arrivals['dep_airport_horiz_distance'].astype('Int64')
    df_arrivals['dep_airport_vert_distance'] = df_arrivals['dep_airport_vert_distance'].astype('Int64')
    df_arrivals['arr_airport_horiz_distance'] = df_arrivals['arr_airport_horiz_distance'].astype('Int64')
    df_arrivals['arr_airport_vert_distance'] = df_arrivals['arr_airport_vert_distance'].astype('Int64')

    df_arrivals.drop(['dep_airport_candidates', 'dep_airport_candidates'], axis=1, inplace=True)  
      
    return df_arrivals


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
