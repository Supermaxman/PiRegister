﻿from CashRegister import *
import sys
import RPi.GPIO as GPIO
import atexit
class UsageException(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv = None):
    if argv is None:
        argv = sys.argv
    #try:
    register = CashRegister("Items.txt")
    #except:
    #    print("Unknown error: ", sys.exc_info()[0])
    #    return 2
    return 0
@atexit.register
def quit():
    GPIO.cleanup()
if __name__ == "__main__":
    sys.exit(main())




