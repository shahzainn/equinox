def checkCMD(cmd):

    if cmd[0:3] == "get":
        return "get"

    elif cmd[0:3] == "cal":
        return "cal"
    
    elif cmd[0:3] == "rem":
        return "rem"
