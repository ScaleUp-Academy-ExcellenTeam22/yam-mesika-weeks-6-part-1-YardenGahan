def get_num() -> list:
    """This function returns list of 2 lists"""
    list1 = [chr(num) for num in range(ord('A'), ord('['))]
    list2 = [chr(num) for num in range(ord('a'), ord('{'))]
    return list1 + list2

if __name__ == "__main__":
    print(get_num())
