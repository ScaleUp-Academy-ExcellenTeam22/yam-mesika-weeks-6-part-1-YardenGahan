"""
This program receives list of numbers from the user, then returns only the positive numbers.
"""


def get_positive_numbers():
    numbers_list = input("enter list of numbers suppurated with ',' : ")
    user_list = numbers_list.split(',')

    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = int(user_list[i])

    positive_numbers = filter(lambda n: n > 0, user_list)
    return tuple(positive_numbers)


print(get_positive_numbers())
