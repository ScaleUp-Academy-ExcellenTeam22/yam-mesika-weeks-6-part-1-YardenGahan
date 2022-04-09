import time


def timer(func, parameter):
    start_time = time.time()
    func(parameter)

    print(f"It took {time.time() - start_time} seconds for the function to run")