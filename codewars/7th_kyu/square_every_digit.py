'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''

def square_digits(num):
    concatenated_number=''
    for item in str(num):
        squared = int(item) * int(item)
        concatenated_number += str(squared)
    # print(concatenated_number)
    return int(concatenated_number)

square_digits(9119)#, 811181