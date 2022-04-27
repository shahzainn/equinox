def remove(cmd):
    
    package = cmd[4:]

    filepath = package + ".py"

    isValid = True

    if isValid:

        file = open("avail-packages.txt")
        packages = file.readlines()
        file.close()

        if package not in packages:
            print("Package not in activated list!")
            quit()

        with open("avail-packages.txt","r+") as f:

            new_f = f.readlines()
            f.seek(0)

            for line in new_f:
                if package not in line:
                    f.write(line)
            
            f.truncate()

        print(package + " remove complete.")