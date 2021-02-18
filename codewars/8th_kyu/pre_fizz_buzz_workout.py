'''
https://www.codewars.com/kata/569e09850a8e371ab200000b/train/python
This is the first step to understanding FizzBuzz.

Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.

Your expected output is an array of positive integers from 1 to n (inclusive).

Your job is to write an algorithm that gets you from the input to the output.
'''

def pre_fizz(n):
    new_list = []
    for number in range(n):
        new_list.append(number + 1)
    print(new_list)
    return new_list

if __name__ == '__main__':
    pre_fizz(1)
    pre_fizz(2)
    pre_fizz(3)
    pre_fizz(4)
    pre_fizz(5)