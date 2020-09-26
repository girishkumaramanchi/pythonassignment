"""class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == complement:
                    return [i, j]
"""


class Solution:
    def twoSum(self, nums, target):
        # mydict = {}
        # for i in range(len(nums)):
        #     mydict[i] = nums[i]
        for i in range(len(nums)):
            complement = target - nums[i]
            j = nums.index(complement)
            if complement in nums and j != i:
                return [i, j]
        return "No two sum element"


nums = [3, 2, 4, 6]
target = 6
ret = Solution().twoSum(nums, target)
print(ret)

