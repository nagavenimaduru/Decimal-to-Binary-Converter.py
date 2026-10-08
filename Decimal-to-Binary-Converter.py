print("Decimal to Binary Converter")
print("---------------------------")

decimal = int(input("Enter a decimal number: "))

if decimal >= 0:
    binary = bin(decimal)[2:]

    print("\nResult:")
    print("Decimal:", decimal)
    print("Binary :", binary)
else:
    print("Please enter a non-negative integer.")
