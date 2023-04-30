from mage_ai.orchestration.triggers.api import trigger_pipeline

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@custom
def transform_custom(*args, **kwargs):
    trigger_pipeline(
        'load_arrivals',
        variables={},
        check_status=False,
        error_on_failure=False,
        poll_interval=60,
        poll_timeout=300,
        verbose=True,
    )

    trigger_pipeline(
        'load_departures',
        variables={},
        check_status=False,
        error_on_failure=False,
        poll_interval=60,
        poll_timeout=300,
        verbose=True,
    )

    return 1



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
