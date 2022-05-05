from audioop import mul
from msilib.schema import Binary

def main():

    def denary_binary():
        bit = int(input("Number Of Bits: "))
        binary = input("Binary: ")

        perDigit_binary = []

        for x in binary:
            
            if x == " ":
                continue
            else:
                perDigit_binary.append(x)

        denary = 0

        while len(perDigit_binary) != bit:
            print("Incorrect binary input - you inputted " + str(len(binary)) + " bits when it should be " + str(bit) + " bits. Try again.")
            binary = input("Binary: ")

        for byte in perDigit_binary:

            if byte == " ":
                continue

            denary = denary * 2 + int(byte)
        
        print("")
        print(binary + " in denary is: " + str(denary))
    
    def binary_denary():

        denary = int(input("Denary: "))
        den_ori = denary
        binary = ""

        while denary > 0:
            
            binary = str(denary % 2) + binary
            denary = denary // 2 
        
        print("")
        print(str(den_ori) + " in binary is " + binary)
    
    def hexa_binary():

        hexa = input("Hexadecimal: ")
        bStr = ""

        n = int(hexa, 16)

        while n > 0:
            bStr = str(n % 2) + bStr
            n = n >> 1
        
        res = bStr

        print(hexa + " in binary is " + res)
    
    def binary_hexa():

        binary = input("Binary: ")
        denary = 0

        perDigit_binary = []

        for x in binary:
            
            if x == " ":
                continue
            else:
                perDigit_binary.append(x)
    
        for byte in perDigit_binary:

            if byte == " ":
                continue

            denary = denary * 2 + int(byte)
        
        ans = hex(denary).split("x")[-1]
        print(binary + " in hexadecimal is " + str(ans))

    def hexa_denary():

        denary = input("Hexadecimal: ")
        res = int(denary, 16)
        print(denary + " in denary is " + str(res))

    def denary_hexa():

        denary = int(input("Denary: "))
        ans = hex(denary).split("x")[-1]
        print(str(denary) + " in hexadecimal is " + str(ans))

    def binary_arithmetic():

        def multiplication():
            firstnumber = input("First Number: ")
            secondnumber = input("Second Number: ")

            multiplication = int(firstnumber, 2) * int(secondnumber, 2)
            binary = bin(multiplication)

            print(firstnumber + " x " + secondnumber + " = " + str(binary[2:]))
        
        def addition():
            firstnumber = input("First Number: ")
            secondnumber = input("Second Number: ")

            sum = bin(int(firstnumber, 2) + int(secondnumber, 2))
            print(firstnumber + " + " + secondnumber + " = " + str(sum[2:]))
        
    
    
    