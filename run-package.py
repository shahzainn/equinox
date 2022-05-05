filepath = "avail-packages.txt"

file = open(filepath)
files = file.readlines()
file.close()

def fetchPackages():

    filepath = "avail-packages.txt"
    file = open(filepath)
    files = file.readlines()

    for packageName in files:

        packageChecker = __import__("fetch-packages")
        packageChecker.checkPackageExists(packageName)

def main():

    packages = []

    print("")
    print("We have these packages available! ")
    print("")
    
    i = 0

    for x in files:

        package = []

        for letter in x:
            package.append(letter)

        if package[len(package) - 1] == "\n":
            package.pop(len(package) - 1)

        n = ""

        for x in package:
            n += x

        packages.append(n)
        i += 1

        print(str(i) + ". " + n)

    print("")
    choice = int(input("Package: "))

    pack = __import__(packages[choice - 1])
    print("")
    pack.main()
