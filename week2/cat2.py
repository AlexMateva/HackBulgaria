# cat2.py
import sys


def main():
    for argument in sys.argv[1::]:
        filename = argument
        data = open(filename, 'r')
        print(data.read())
        data.close()
        print('\n')

if __name__ == '__main__':
    main()