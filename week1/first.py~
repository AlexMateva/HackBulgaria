def sum_of_digits(n):

    result = 0
    if n < 0:
        n = -1 * n
    while n >= 1:
        result += n % 10
        n = n // 10
    return result
sum_of_digits(-146)


def count_digits(n):
    counter = 0

    for i in str(n):
        counter += 1

    return counter


def to_number(digits):
    result = 0

    for digit in digits:
        power = count_digits(digit)
        result = result * (10 ** power) + digit

    return result


def fact(n):
    result = 1
    while(n >= 1):
        result = result * n
        n = n - 1
    return result


def fact_digits(n):
    result = 0
    if n < 0:
        n = (-1 * n)
    while n >= 1:
        result += fact(n % 10)
        n = n // 10
    return result
fact_digits(145)


def fibonacci(n):
    lst = [1, 1]
    if n == 1:
        return lst[1::]
    for iter in range(2, n):
        lst.append(lst[iter - 1] + lst[iter - 2])
    return lst


def fib_number(n):
    return to_number(fibonacci(n))


def palindrome(obj):
    return str(obj) == str(obj)[::-1]


def count_vowels(str):
    result = 0

    for ch in str.lower():
        if ch in "aeiouy":
            result += 1

    return result


def count_consonants(str):
    result = 0

    for ch in str.lower():
        if ch in "bcdfghjklmnpqrstvwxz":
            result += 1
    return result


def char_histogram(string):

    histogram = {}
    for ch in string:
        histogram[ch] = 0
    for ch in string:
        histogram[ch] += 1
    return histogram


def to_digits(n):
    return [int(x) for x in str(n)]
