'''
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''

def move_zeros(array):
    new_array = []
    zero_array = []
    
    for item in array:
        if item == 0:
            zero_array.append(item)
        else:
            new_array.append(item)
    for item in zero_array:
        new_array.append(item)
    print(new_array)
    return new_array

if __name__ == '__main__':
    move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1])