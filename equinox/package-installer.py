def checkPackageExists(package):

    try:

        filepath = open(package)
        filepath.close()

        return True

    except FileNotFoundError:

        print("File does not exist!")
        return False

def install(cmd):
    
    package = cmd[4:]

    filepath = package + ".py"

    isValid = checkPackageExists(filepath)

    if isValid:

        file = open("avail-packages.txt")
        packages = file.readlines()
        file.close()

        if package in packages:
            print("Package already installed!")
            quit()

        file = open("avail-packages.txt", "a")
        file.write("\n" + package)
        file.close()

        print(package + " install complete.")