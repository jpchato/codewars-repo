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
    results = []
    while len(snail_map) > 0:
        # go right
        results += snail_map[0]
        del snail_map[0]

        if len(snail_map) > 0:
            # go down
            for i in snail_map:
                results += [i[-1]]
                del i[-1]
            # go left
            if snail_map[-1]:
                # print('snail_map[-1][::-1] = ', snail_map[-1][::-1])
                # appending the last array in reversed order
                results += snail_map[-1][::-1]
                del snail_map[-1]
            # go top
            for i in reversed(snail_map):
                results += [i[0]]
                del i[0]
    return results


   

if __name__ == '__main__':
    snail([[1,2,3],
         [4,5,6],
         [7,8,9]])
        #  expected = [1,2,3,6,9,8,7,4,5]
