
from src.constante import FAILURE, SUCCESS

def printUsage():
    print("USAGE\n\t./301dannon file\nDESCRIPTION\n\tfile\t", end="")
    print("file that contains the numbers to be sorted, separated by spaces")


def advenced_parsing(list):
    string = list
    for ch in string:
        if not ch.isdigit() and not ch in [".", "-", " "]:
            string = string.replace(ch, " ")
    return string.split()


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

    if not buff or buff[0] == '':
        exit(FAILURE)
    try:
        list = [float(n) for n in buff]
    except:
        print("Error list argument")
        exit(FAILURE)
    return list