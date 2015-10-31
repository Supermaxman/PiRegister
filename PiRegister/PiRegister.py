from CashRegister import *
import sys

class UsageException(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv = None):
    if argv is None:
        argv = sys.argv
    try:
        register = CashRegister("Items.txt")
    except:
        print("Unknown error: ", sys.exc_info()[0])
        return 2
    return 0
if __name__ == "__main__":
    sys.exit(main())




