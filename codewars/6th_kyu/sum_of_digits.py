'''
https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''

# loop through stringified version of n and sum all the integerized numbers
# if the sum is greater than 10, do it again ad nauseum

def digit_sum(n):
    '''(int)->number
    Returns the sum of all the digits in the given integer, n'''
    if n<10:
        return n
    return n%10 + digit_sum(n//10)

def digital_root(n):
    if n < 10:
        return n
    return digital_root(digit_sum(n))


        
if __name__ == '__main__':
    # digital_root(16)
        # 7
    digital_root(942)
        # 6