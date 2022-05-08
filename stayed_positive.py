def get_positive_numbers():
    """
    This function receives list of numbers from the user, then returns only the positive numbers.
    @return: tuple of positive numbers
    """
    numbers_list = input("enter list of numbers suppurated with ',' : ")
    user_list = numbers_list.split(',')

    # convert each item to int type
    [user_list[i] = int(user_list[i]) for i in range(len(user_list))]

    return tuple(filter(lambda n: n > 0, user_list))


if __name__ == "__main__":
    print(get_positive_numbers())
