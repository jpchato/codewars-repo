'''
Objective
Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.
'''

def array_madness(a,b):
    squared = 0
    cubed = 0
    for item in a:
        squared += item ** 2
    for item in b:
        cubed += item ** 3
    # if squared > cubed:
    #     return True
    # else:
    #     return False
    print(True if a > b else False)
    return True if a > b else False
if __name__ == '__main__':
    array_madness([4, 5, 6], [1, 2, 3])#,True
    array_madness( [1, 2, 3],[4, 5, 6])#,False