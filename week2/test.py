def main():
    filename = 'panda.txt'
    data = open(filename, 'w')
#    with open(fileneme, 'w') as data:
    data.write("Hello, I'm Panda\n")
    data.close()

if __name__ == '__main__':
    main()
