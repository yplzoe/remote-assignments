def twoSum(nums, target):
    left = 0
    right = len(nums)-1
    cur_sum = nums[left]+nums[right]
    while cur_sum != target:
        if cur_sum < target:
            left += 1
        else:
            right -= 1
        cur_sum = nums[left]+nums[right]

    return [left, right]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 7, 11, 15], 18))
# Time Complexity: O(n)
