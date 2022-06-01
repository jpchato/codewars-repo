#Problem Domain: Return a running sum of an array

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        new_array = []
        for count, number in enumerate(nums):
            print(count)
            if count != 0:
                print(number, new_array[count - 1])
                print(f"appending {number + new_array[count - 1]}")
                new_array.append(number + new_array[count - 1])
            else:
                new_array.append(number)
        return new_array