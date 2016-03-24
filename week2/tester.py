import sys
def main():
    filename = sys.argv[1]
    data = open(filename, 'r')

    print(data.read())

    data.close()

#    with open(filename, 'r') as 


if __name__ == '__main__':
    main()
