'''
2-
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary 
representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

def um_bin():
    decimal = int(input("Número Decimal: "))
    binario = bin(decimal)
    num_um = 0
    for a in str(binario):
        if a == "1":
            num_um += 1
    print(num_um)
um_bin()