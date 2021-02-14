'''
It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.
'''
import math

def array_mean():
    sum = 0
    my_array = [1, 5, 87, 45, 8, 8]
    for item in my_array:
        sum += item
    mean = math.floor(sum/len(my_array))
    print(mean)
    return mean

if __name__ == "__main__":
    array_mean()