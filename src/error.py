
from src.constante import FAILURE, SUCCESS

def printUsage():
    print("USAGE\n\t./301dannon file\nDESCRIPTION\n\tfile\t", end="")
    print("file that contains the numbers to be sorted, separated by spaces")


def advenced_parsing(list):
    cpy = list
    sep = " "
    for char in cpy:
        if not char.isdigit() and char != "." and char != "-":
            sep = char
            break
    number = cpy.split(sep, 1)
    try:
        return [float(number[0])] + advenced_parsing(number[1])
    except:
        try:
            return advenced_parsing(number[1])
        except:
            return [float(number[0])]


def error(argv):
    if "-h" in  argv or "--help" in argv:
        printUsage()
        exit(SUCCESS)
    if (len(argv) != 1):
        exit(FAILURE)
    try:
        fd = open(argv[0], "r")
        buff = fd.read().rstrip()
        buff = advenced_parsing(buff)
    except:
        print("Error file doesn't exists")
        exit(FAILURE)

    if buff[0] == '':
        exit(FAILURE)
    try:
        list = [float(n) for n in buff]
    except:
        print("Error list argument")
        exit(FAILURE)
    return list