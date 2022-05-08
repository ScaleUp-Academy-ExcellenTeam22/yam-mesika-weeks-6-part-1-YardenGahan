import time


def timer(func, parameter) ->str:
    """
    The function counts the time it takes a given function to run.
    @param func: functions.
    @param parameter: parameter for func.
    @return: The amount of time it tooks for func to run.
    """
    start_time = time.time()
    func(parameter)

    return(f"It took {time.time() - start_time} seconds for the function to run")
    
