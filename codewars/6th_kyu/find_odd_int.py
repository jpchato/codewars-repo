'''
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''
def find_it(seq):
    odd_dict = {
    }   
    for number in seq:
        if number not in odd_dict:    
            odd_dict[number] = 1
        elif number in odd_dict:
            odd_dict[number] += 1
    for key, value in odd_dict.items():
        if value % 2 != 0:
            return key
    

if __name__== '__main__':
    find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
    find_it([10])