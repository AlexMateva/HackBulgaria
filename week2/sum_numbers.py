# sum_numbers.py
import sys


def main():
    numbers = ''
    s = 0
    filename = sys.argv[1]
    data = open(filename, 'r')
    numbers = data.read()
    numbers = numbers.split(' ')
    for i in range(0, len(numbers)):
        if numbers[i].isdigit():
            s += int(numbers[i])
    print(s)

if __name__ == '__main__':
    main()