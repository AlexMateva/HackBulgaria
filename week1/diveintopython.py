

def is_number_balanced(digits):
    a = 0
    b = 0
    for i in range(0, len(str(digits)) // 2):
        a += int(str(digits)[i])

    if len(str(digits)) % 2 == 0:
        for i in range(len(str(digits)) // 2, len(str(digits))):
            b += int(str(digits)[i])
    else:
        for i in range(len(str(digits)) // 2 + 1, len(str(digits))):
            b += int(str(digits)[i])

    return a == b


def is_increasing(seq):
    for i in range(0, len(seq) - 1):
        if(seq[i] >= seq[i + 1]):
            return False
        else:
            continue
    return True


def is_decreasing(seq):
    for i in range(0, len(seq) - 1):
        if(seq[i] <= seq[i + 1]):
            return False
        else:
            continue
    return True


def get_largest_palindrome(n):
    for i in range(n - 1, 0, -1):
        if str(i) == str(i)[::-1]:
            return i
        else:
            continue
    return 0


def prime_numbers(n):
    all_numbers = [x for x in range(2, n + 1)]

    for i in range(2, n+1):
        not_prime = [x for x in range(i*2, n+1, i)]
        all_numbers = set(all_numbers) - set(not_prime)

    return sorted(list(all_numbers))


def char_histogram(string):

    histogram = {}
    for ch in string:
        histogram[ch] = 0
    for ch in string:
        histogram[ch] += 1
    return histogram


def is_anagram(a, b):
    a = a.lower()
    b = b.lower()
    return char_histogram(a) == char_histogram(b)


def birthday_ranges(birthdays, ranges):
    result = []

    for r in ranges:
        counter = 0

        for day in birthdays:
            if day in range(r[0], r[1] + 1):
                counter += 1

        result.append(counter)

    return result


def sum_matrix(m):
    result = 0

    for row in m:
        for num in row:
            result += num
    return result


def position_bombing_result(m, i, j):
    num_rows, num_cols = len(m), len(m[i])
    min_i, min_j = max(0, i - 1), max(0, j - 1)
    max_i, max_j = min(i+1, num_rows), min(j+1, num_cols)
    s = 0
    for r in range(0, num_rows):
        for c in range(0, num_cols):
            if r == i and c == j:
                d = m[r][c]
            elif r >= min_i and r <= max_i and c >= min_j and c <= max_j:
                d = max(0, m[r][c] - m[i][j])
            else:
                d = m[r][c]
            s += d
    return s


def matrix_bombing_plan(m):
    result = {}
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            result[(i, j)] = position_bombing_result(m, i, j)
    return result


print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def is_transversal(transversal, family):
    for group in family:
        it = [x for x in group if x in transversal]
        if len(it) == 0 or len(it) > 1:
            return False
    return True
