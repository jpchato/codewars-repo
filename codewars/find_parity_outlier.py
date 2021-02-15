'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''

def find_outlier(integers):
    even_list = []
    odd_list = []
    for number in integers:
        if number % 2 == 0:
            even_list.append(number)
        if number % 2 != 0:
            odd_list.append(number)
    if len(even_list) == 1:
        print (even_list[0])
        return (even_list[0])
    elif len(odd_list) == 1:
        print (odd_list[0])
        return (odd_list[0])

if __name__ == "__main__":
    find_outlier([2, 4, 6, 8, 10, 3])
    find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
    find_outlier([160, 3, 1719, 19, 11, 13, -21])