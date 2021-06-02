'''
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
'''

def positive_sum(arr):
    # Your code here
    total = 0
    for item in arr:
        if item > 0:
            total += item
    if total == 0:
        return 0
    else:
        return total

print(positive_sum([1,2,3,4,5]),15)