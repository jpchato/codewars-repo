class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for count, item in enumerate(nums):
            ans.append(nums[nums[count]])
        print(ans)
        return ans
    
Solution().buildArray([0,2,1,5,3,4])