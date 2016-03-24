# generate_numbers.py
import sys
from random import randint


def main():

    filename = sys.argv[1]
    data = open(filename, 'w')
    n = int(sys.argv[2])
    for i in range(0, n):
        number = randint(1, 1000)
        data.write(str(number))
        data.write(' ')
    data.close()

if __name__ == '__main__':
    main()