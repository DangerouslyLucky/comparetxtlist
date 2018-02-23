import argparse


def main():

    args = parser()

    if args.file1 == "no_file1":
        file1 = input("Enter the name of the first list: ")
    else:
        file1 = args.file1
    if args.file2 == "no_file2":
        file2 = input("Enter the name of the second list: ")
    else:
        file2 = args.file2

    output = []

    lines1 = load_file(file1)
    lines2 = load_file(file2)

    for line in lines1:
        if line in lines2:
            output.append(line)

    print("Lines found in both lists:\n")
    for line in output:
        print(line)


# create the parser and return args
def parser():

    # Create the argument parser
    parser = argparse.ArgumentParser(description=(
        'Scott Cuthbert - Compare Lists'))
    parser.add_argument('-1', dest='file1', nargs='?',
                        action='store', default='no_file1',
                        help='defines a filename to run against')
    parser.add_argument('-2', dest='file2', nargs='?',
                        action='store', default='no_file2',
                        help='defines a filename to run against')

    # Create object args to reference
    args = parser.parse_args()

    return args


# load file return list of lines
def load_file(filename):

    fileLines = []

    with open(filename) as readfile:
        for line in readfile:
            fileLines.append(line.strip())

    return fileLines


main()
