def checkPackageExists(package):

    try:

        new_package = ""
        package_name = []

        for letter in package:
            package_name.append(letter)

        if package_name[len(package_name) - 1] == "\n":
            package_name.pop(len(package_name) - 1)

        print(package_name)

        for letter in package_name:
            new_package += letter

        filepath = open(new_package + ".py")
        print(new_package + " fetched.")
        filepath.close()

        return True

    except FileNotFoundError:

        print(new_package + " does not exist!")
        return False