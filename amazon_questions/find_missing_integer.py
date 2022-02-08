'''
1. Find the missing number in the array
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution.
'''

def find_missing(input):
    #TODO: Write - Your - Code
    input = sorted(input)
    print(input)
    expected_total = 0
    actual_total = 0
    for number in input:
        actual_total += number
    for i in range(1, input[-1] + 1):
        expected_total += i
        print(i)
    print(expected_total, actual_total)
    print(expected_total - actual_total)    
    return expected_total - actual_total

find_missing([3, 7, 1, 2, 8, 4, 5])