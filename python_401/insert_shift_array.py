import unittest
'''
Feature Tasks
Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.
Example
Input	Output
[2,4,6,-8], 5	[2,4,5,6,-8]
[42,8,15,23,42], 16	[42,8,15,16,23,42]
'''

def insert_shift_array(arr, val):
    if len(arr)%2 == 0:
        middle = len(arr)//2
        first_half = arr[:middle]
        second_half = arr[middle:]
        
        first_half.append(val)
        # print(first_half, second_half)
        answer = first_half + second_half
        # print(answer)
        return answer
    else:
        middle = (len(arr)//2)
        first_half = arr[:middle+1]
        second_half = arr[middle+1:]
        # print(first_half, second_half)
        first_half.append(val)
        
        answer = first_half + second_half
        # print(answer)
        return answer

# insert_shift_array([2,4,6,-8], 5)
# insert_shift_array([42,8,15,23,42], 16)
class Test(unittest.TestCase):
    def test_test(self):
        self.assertEqual(insert_shift_array([2,4,6,-8], 5), [2,4,5,6,-8])
        self.assertEqual(insert_shift_array([42,8,15,23,42], 16), [42,8,15,16,23,42])
         
         

if __name__ == '__main__':
    unittest.main()