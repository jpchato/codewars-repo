'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''
def grow(arr):
    product = 1
    for number in arr:
        product *= number
    print(product)
    return product

if __name__ == '__main__':
    grow([1, 2, 3])
    grow([4, 1, 1, 1, 4])
    grow([2, 2, 2, 2, 2, 2])