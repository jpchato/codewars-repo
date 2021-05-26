
def containsDuplicate(nums):
    check_dict = {

    }
    for item in nums:
        # print(item)
        if item not in check_dict:
            check_dict[item] = 1
        else:
            return True
    return False

print(containsDuplicate( [1,2,3,1]))
