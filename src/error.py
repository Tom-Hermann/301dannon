
from src.constante import FAILURE, SUCCESS

def printUsage():
    print("USAGE\n\t./301dannon file\nDESCRIPTION\n\tfile\t", end="")
    print("file that contains the numbers to be sorted, separated by spaces")

def error(argv):
    if "-h" in  argv or "--help" in argv:
        printUsage()
        exit(SUCCESS)
    if (len(argv) != 1):
        exit(FAILURE)
    try:
        fd = open(argv[0], "r")
        buff = fd.read().rstrip()
        buff = ' '.join(buff.split()).split(' ')
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