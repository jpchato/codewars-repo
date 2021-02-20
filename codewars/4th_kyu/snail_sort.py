'''
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
python slicing: [start:end:step]
'''

def snail(snail_map):
    new_array= []
    for item in snail_map[0]:
        new_array.append(item)
    for array in snail_map[1:-1:]:
        new_array.append(array[-1])
    for item in snail_map[-1][::-1]:
        new_array.append(item)
    for array in snail_map[-2:0:-1]:
        # print(array)
        new_array.append(array[0])
    print(new_array)

if __name__ == '__main__':
    snail([[1,2,3],
         [4,5,6],
         [7,8,9]])
        #  expected = [1,2,3,6,9,8,7,4,5]

# def snail(snail_map):
#     new_array = []
#     for item in snail_map[0]:
#        new_array.append(item)
#     new_array.append(snail_map[1][-1])
#     for item in snail_map[-1][::-1]:
#         new_array.append(item)
#     for item in snail_map[1][0:2:]:
#         new_array.append(item)
#     print(new_array)
#     return new_array

# algorithm
# the first array is added to the new array in sequential order
# the last element of the remaining arrays is added to the new array until we reach the last array
# the last array is then added in reverse order to the new array
# then the first element of the remaining arrays is added (in reverse order)