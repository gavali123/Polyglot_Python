import math


def is_right_truncatable(num):
    str_num = str(num)
    size = len(str_num) - 1
    is_right_truncate = True
    for i in range(size, 0, -1):
        if not is_prime(int(str_num[0: i])):
            is_right_truncate = False
    return is_right_truncate


def is_left_truncatable(num):
    str_num = str(num)
    size = len(str_num)
    is_left_truncate = True
    for i in range(1, size):
        if not is_prime(int(str_num[i:])):
            is_left_truncate = False
            break
    return is_left_truncate


def two_sided_prime(num):
    if not is_prime(num):
        return False
    if is_left_truncatable(num) and is_right_truncatable(num):
        return True
    return False


def is_prime(num):
    if num <= 1:
        return False;
    if num == 2:
        return True;
    if num > 2 and num % 2 == 0:
        return False
    max_limit = math.floor(math.sqrt(num)) + 1
    for i in range(3, max_limit, 2):
        if num % i == 0:
            return False
    return True
