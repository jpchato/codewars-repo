'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

# print(bin(1234)[2:])

# def count_bits(n):
#     n = 1234
#     bits = bin(1234)[2:]
#     # print(bits)
#     sum = 0
#     for num in bits:
#         sum += int(num)
#     print(sum)

def count_bits(n):
#     n = 1234
    bits = bin(n)[2:]
    # print(bits)
    sum = 0
    for num in bits:
        sum += int(num)
    return sum
    # print(sum)

if __name__ == "__main__":
    count_bits(10)