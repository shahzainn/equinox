
packages = ["binary", "circle"]

import math
import string
import random

from math import *
from string import *
from random import *

def checkCMD(cmd):

    if cmd[0:3] == "get":
        return False

    elif cmd[0:3] == "cal":
        return True

def interface():

    cmd = input()
    cmd_low = cmd.lower()

    command_handler = __import__("command-handler")
    valid_cmd = command_handler.checkCMD(cmd_low)

    if valid_cmd == "get":
        package_installer = __import__("package-installer")
        package_installer.install(cmd)

    elif valid_cmd == "cal":
        calculator = __import__("run-package")
        calculator.fetchPackages()
        calculator.main()

    elif valid_cmd == "rem":
        package_remover = __import__("package-remover")
        package_remover.remove(cmd)

    else:
        print("Invalid Input.")

while True:
    interface()