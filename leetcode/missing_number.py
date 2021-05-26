def missingNumber(nums):
    nums.sort()
    nums_dict = {

    }
    
    for item in nums:
        nums_dict[item] = 1
    # for item in nums_dict:
    #     if item + 1 not in nums_dict:
    #         return item + 1
    for num in range(0, nums[-1] + 2):
        print(num)
        if num not in nums_dict:
            return num

# print(missingNumber([3,0,1]))
# print(missingNumber([1]))
print(missingNumber([0, 1]))