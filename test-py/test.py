"""
Test file to play with open-sky api
"""

from datetime import datetime, timezone
import pandas as pd
# from opensky_api import OpenSkyApi
# import secret_file as sf


def run_api():
    """
    function to extract data from api
    """
    # get api client
    # api = OpenSkyApi(username=sf.username, password=sf.password)
    # set requested vars
    # start_time = 1681112694
    # end_time = 1681199094
    # airport = "LLBG"
    # # https://opensky-network.org/api/flights/departure?airport=LLBG&begin=1681112694&end=1681285494
    # # get arrivals
    # flights = api.get_arrivals_by_airport(airport, start_time, end_time)
    # flight_list = []
    # for flight in flights:
    #     temp_lst = [ flight.icao24, flight.callsign, 
    #                 flight.firstSeen, flight.estDepartureAirport, 
    #                 flight.lastSeen, flight.estArrivalAirport, 
    #                 flight.estDepartureAirportHorizDistance,
    #                 flight.estDepartureAirportVertDistance, 
    #                 flight.estArrivalAirportHorizDistance, 
    #                 flight.estArrivalAirportVertDistance,
    #     ]
    #     flight_list.append(temp_lst)
    # # create df
    # df_arrivals = pd.DataFrame(
    #     flight_list,
    #     columns=[ "icao24", "callsign", "first_seen", 
    #         "dep_airport", "last_seen", "arr_airport", 
    #         "dep_airport_horiz_distance", "dep_airport_vert_distance",
    #         "arr_airport_horiz_distance", "arrival_airport_vert_distance",
    #     ],
    # )
    # # print out data
    # print(df_arrivals.head())
    # print(len(df_arrivals))


def run_json():
    """
    function to extract data from local json files
    """
    cols = [ "icao24", "first_seen", "departure_airport", "last_seen", 
            "arr_airport", "callsign", "dep_airport_horiz_distance",
            "dep_airport_vert_distance", "arr_airport_horiz_distance", 
            "arrival_airport_vert_distance", "dep_airport_candidates", "arr_airport_candidates",
    ]

    # arrivals
    df_arrivals = pd.read_json("data/arrivals.json")
    df_arrivals.columns = cols
    df_arrivals.drop(
        ["dep_airport_candidates", "arr_airport_candidates"], axis=1, inplace=True
    )
    print(f"Len arrivals {len(df_arrivals)}")
    print(df_arrivals.head())

    # departures
    df_departure = pd.read_json("data/departure.json")
    df_departure.columns = cols
    df_departure.drop(
        ["dep_airport_candidates", "arr_airport_candidates"], axis=1, inplace=True
    )

    print(f"Len departures {len(df_departure)}")
    print(df_departure.head())


def load_airports() -> pd.DataFrame:
    """
    function to extract data from local airports.dat
    """
    df_airports = pd.read_csv(
        "data/airports.dat",
        na_values=["\\N", "Null"],
        names=[ "airport_id",  "name", "city", "country", "iata",
               "icao", "lat", "long", "altitue_(feet)", "timezone",
               "dst", "tz", "type", "source"],
    )
    df_airports.drop(["type", "source"], axis=1, inplace=True)
    print(df_airports.head())
    print(f"Len = {len(df_airports)}")
    # print(df_airports.info())
    # print(df_airports.describe())
    # print(f"Isnull = \n{df_airports.isnull().sum()}")
    # print(df_airports[df_airports["icao"].isna()])
    # print(df_airports[df_airports.isna().any(axis=1)])
    # print(df_airports['source'].unique())
    return df_airports


def load_airlines() -> pd.DataFrame:
    """
    function to extract data from local airlines.dat
    """
    df_airlines_full = pd.read_csv(
        "data/airlines.dat",
        na_values=["\\N", "Null"],
        skiprows=1,  # skip first empty airline
        names=["airline_id", "name", "iata", "icao", "callsign", "country", "active"],
    )

    df_airlines = df_airlines_full.copy()[df_airlines_full["active"] == "Y"]
    df_airlines.drop(["active"], axis=1, inplace=True)
    print(df_airlines.head())
    print(f"Len = {len(df_airlines)}")
    # print(df_airlines.info())
    # print(df_airlines.describe())
    # print(f"Isnull = \n{df_airlines.isnull().sum()}")
    # print(df_airlines[ df_airlines['icao'].isna() ])
    # print(df_airlines[~(df_airlines.isna().any(axis=1))])
    # print(df_airlines[(~df_airlines.isna()).any(axis=1)])
    # print(df_airlines['name'].unique())
    return df_airlines


def load_routes() -> pd.DataFrame:
    """
    function to extract data from local routes.dat
    """
    df_routes_full = pd.read_csv(
        "data/routes.dat",
        na_values=["\\N", "Null"],
        names=[ "airline_code", "airline_id", "src_airport", "src_airport_id",
               "dst_airport", "dst_airport_id", "codeshare", "stops", "equipment" ],
        dtype={
            "airline_id": "Int64",
            "src_airport_id": "Int64",
            "dst_airport_id": "Int64",
        },
    )
    df_routes = df_routes_full.copy()[
        (
            (df_routes_full["src_airport"] == "TLV")
            | (df_routes_full["dst_airport"] == "TLV")
        )
        & (df_routes_full["airline_id"] == 2150)
    ]
    # df_airlines.drop(["active"], axis=1, inplace=True)
    print(df_routes.head(100))
    print(f"Len = {len(df_routes)}")
    # print(df_routes.info())
    # print(df_routes.describe())
    # print(f"Isnull = \n{df_routes.isnull().sum()}")
    # print(df_routes['codeshare'].unique())
    # print(f"stops = \n{df_routes.groupby(['stops'])['airline_code'].count()}")
    return df_routes


def get_unix_time():
    """
    funcation to get unix time for specific dates
    """
    # print(datetime.now().timestamp())
    print(f"now = {int(datetime.now().timestamp())}")

    jan_1 = datetime(2023, 1, 1, 0, 0, tzinfo=timezone.utc)
    jan_2 = datetime(2023, 1, 2, 0, 0, tzinfo=timezone.utc)

    print(f"jan_1 = {int(jan_1.timestamp())}")
    print(f"jan_2 = {int(jan_2.timestamp())}")


def get_dat_files():
    """
    wrapper function to extract data from all local files
    """
    # data from openflights.org/data.html
    # load_airports()
    # load_airlines()
    # load_routes()



if __name__ == "__main__":
    # run_json()
    # get_dat_files()
    get_unix_time()
