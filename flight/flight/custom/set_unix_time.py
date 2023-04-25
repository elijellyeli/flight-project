from datetime import datetime, timedelta, timezone

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    """
    Returns:
        dict start and end time
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
    end_ts = int(yesterday_end.timestamp())
    # start_ts = 1680296400
    # end_ts = 1680382799
    print(f'start_ts={start_ts}')
    print(f'end_ts={end_ts}')    
    return {"start":start_ts, "end":end_ts}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
