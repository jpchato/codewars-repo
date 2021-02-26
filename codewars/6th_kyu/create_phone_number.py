'''
https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
'''

def create_phone_number(n):
    #your code here
    phone_number = '(' + str(n[0]) + str(n[1]) + str(n[2]) + ')' +  ' ' + str(n[3]) + str(n[4]) + str(n[5]) + '-' + str(n[6]) +  str(n[7]) + str(n[8]) + str(n[9])
    print(phone_number)
    return phone_number
    
if __name__ == '__main__':
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    # "(123) 456-7890"
