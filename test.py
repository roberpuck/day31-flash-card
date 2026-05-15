class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in nums:
            second_index = i+1
            if i + nums[second_index] == target:
                result.append(i)

nums=[2,7,11,15]
target =9

sol = Solution()
sol.twoSum(nums,target)
