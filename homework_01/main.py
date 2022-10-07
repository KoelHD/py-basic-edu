"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i ** 2 for i in num]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n == 2:
        return True
    if (n % 2 == 0) or (n == 1):
        return False
    d = 3
    while n % d != 0:
        d += 2
    if n == d:
        return True
    else:
        return False


def filter_numbers(nums, filters):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filters == ODD:
        return [i for i in nums if i % 2 != 0]
    elif filters == EVEN:
        return [i for i in nums if i % 2 == 0]
    else:
        return list(filter(is_prime, nums))
