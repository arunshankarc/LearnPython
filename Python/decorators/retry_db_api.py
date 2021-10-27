"""
[Below code is a pseudocode for connection to db/api and retrying the same.]
"""
def _return_no_parameters(db_api):
    if "db" not in db_api or "api" not in db_api:
        print(f"Unknown parameter passed {db_api}, valid parameters are 'db' or 'api'")
    print(f'Required parameters not found for connection to {db_api}')

def retry_db_api(connect_to):
    """
    [This decorator is a common code for all activities needed while
    retrying connnection to db or api]

    Args:
        connect_to ([str]): [db/api]
    """
    if connect_to == 'db':
        def inner(function):
            def wrapper(*args, **kwargs):
                if not args:
                    return _return_no_parameters('db')
                print("Perform operations needed for db")
                return function(*args, **kwargs)
            return wrapper
        return inner
    elif connect_to == 'api':
        def inner(function):
            def wrapper(*args, **kwargs):
                if not args:
                    return _return_no_parameters('api')
                print("Perform operations needed for api")
                return function(*args, **kwargs)
            return wrapper
        return inner
    else:
        return _return_no_parameters('others')


@retry_db_api(connect_to='api')
def connect_to_db(test_db):
    """[summary]

    Args:
        connect_to ([type]): [description]

    Returns:
        [type]: [description]
    """
    print(f"Connecting to - {test_db}")


connect_to_db('test')
