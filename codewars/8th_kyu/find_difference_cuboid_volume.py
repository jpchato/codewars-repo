'''
https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python
In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.
'''

def find_difference(a, b):
    # Your code here!
    a_volume = 1
    b_volume = 1
    for item in a:
        a_volume *= item
    for item in b:
        b_volume *= item
    
    if a_volume > b_volume:
        return a_volume - b_volume
    else:
        return b_volume - a_volume

if __name__ == '__main__':
    find_difference([3, 2, 5], [1, 4, 4])