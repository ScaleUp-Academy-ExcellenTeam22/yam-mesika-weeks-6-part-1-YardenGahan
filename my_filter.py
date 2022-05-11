def my_filter(func, values : list) -> list:
    """
    This function overloads the function "filter".
    @param func: wanted function to check
    @param values: list of values
    @return: value that in the func
    """
    for val in values:
        if func(val):
            yield val
