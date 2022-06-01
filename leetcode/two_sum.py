class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for count, number in enumerate(nums):
            print(count, number)
        # print(nums)
            print(hash_map)
            if nums[count] in hash_map:
                return [count, hash_map[nums[count]]]
            else:
                hash_map[target-nums[count]] = count
                
# [2,7,11,15]
# 9
# [3,2,4]
# 6
# [3,3]
# 6

# test = Solution()
Solution().twoSum([2,7,11,15], 9)