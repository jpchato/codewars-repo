'''
https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/python
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.
'''

def maps(a):
    for i in range(len(a)):
        a[i] *= 2
    print (a)
    return a


if __name__ == "__main__":
    maps([1, 2, 3])
    maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    maps([])