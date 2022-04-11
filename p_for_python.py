def get_num():
    list1 = [chr(num) for num in range(ord('A'), ord('['))]
    list2 = [chr(num) for num in range(ord('a'), ord('{'))]
    return list1, list2


print(get_num())
