def fetchPackages():

    filepath = "avail-packages.txt"
    file = open(filepath)
    files = file.readlines()

    for packageName in files:

        packageChecker = __import__("fetch-packages")
        packageChecker.checkPackageExists(packageName)
    