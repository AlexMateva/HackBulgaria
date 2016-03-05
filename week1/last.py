def count_words(arr):
    words = {}
    for string in arr:
        if string not in words:
            words[string] = 1
        else:
            words[string] += 1
    return words


def nan_expand(times):
    if times == 0:
        return ""
    result = ""

    for i in range(times):
        result += "Not a "

    return result + "NaN"


def iterations_of_nan_expand(expanded):
    if nan_expand(expanded.count("Not a")) == expanded:
        return expanded.count("Not a")

    return False
# def nan_expand(n):
#     result = ''
#     while n >= 1:
#         result = result + 'Not a '
#         if n == 1:
#             result = result + 'NaN'
#         n = n - 1
#     return result


# def iterations_of_nan_expand(expanded):
#     count = 0
#     if expanded == '':
#         return 0
#     expanded = expanded.split()
#     for char in expanded:
#         if char == 'Not':
#             count += 1
#     if count != 0:
#         return count
#     else:
#         return False


# print(iterations_of_nan_expand("Not a Not a Nan"))


def group2(lst):

    result = []
    small_G = []
    small_G.append(lst[0])

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            small_G.append(lst[i])
        if i == len(lst) - 1 or lst[i] != lst[i - 1]:
            result.append(small_G)
            small_G = []
            small_G.append(lst[i])
    return result


def take_same(items):
    first = items[0]
    n = len(items)
    index = 1
    result = [first]

    while index < n and first == items[index]:
        result.append(items[index])
        index += 1

    return result


def group(items):
    result = []

    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)

        items = items[len(current_group):]

    return result


def max_consecutive(items):
    it = group(items)
    length = 0
    for i in range(0, len(it)):
        if len(it[i]) > length:
            length = len(it[i])
    return length


def sum_of_numbers(string):
    result = 0
    curr = 0

    for char in range(0, len(string)):
        if string[char] >= '0' and string[char] <= '9':
            curr = int(string[char]) + curr * 10

        else:
            result += curr
            curr = 0

    if curr != 0:
        result += curr

    return result


def gas_stations(distance, tank_size, stations):
    result = [0]
    stations.append(distance)

    for i in range(0, len(stations)-1):
        diff = stations[i+1] - stations[i]
        size = tank_size - (stations[i] - result[-1])

        if size < diff:
            result.append(stations[i])
            size = tank_size

    return result[1:]


NUMBERS = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " ",
}


def numbers_to_message(num):
    res = ""
    numbs_groups = group(num)
    up_c = False

    for grp in numbs_groups:
        if grp[0] == 1:
            up_c = True
            continue
        if grp[0] == -1:
            continue

        key_letters = NUMBERS[grp[0]]
        times_pressed = len(grp)
        selected_letter_index = times_pressed % len(key_letters) - 1
        letter = key_letters[selected_letter_index]

        if up_c:
            res += letter.upper()
            up_c = False

        else:
            res += letter

    return res


def symbol_to_list(letter):
    buttons = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

    for button in buttons:

        if letter in button:
            push_button = buttons.index(button) + 2
            press = button.index(letter) + 1
            return [push_button for i in range(press)]


def are_symbols_from_same_button(a, b):
    buttons = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

    for button in buttons:
        if a in button and b in button:

            return True

    return False


def message_to_numbers(message):
    sequence = []
    previous_symbol = ''

    for symbol in message:
        if symbol == ' ':
            sequence.append(0)
        else:
            if are_symbols_from_same_button(previous_symbol.lower(), symbol.lower()):
                sequence.append(-1)
            if symbol == symbol.upper():
                sequence.append(1)
                sequence += symbol_to_list(symbol.lower())
            else:
                sequence += symbol_to_list(symbol)
        previous_symbol = symbol

    return sequence

print(message_to_numbers("aAabbcda"))
print(message_to_numbers("Ivo e panda"))
print(message_to_numbers("aabbcc"))
