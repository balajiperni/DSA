class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            result = target - nums[i]
            if result in nums and nums.index(result)!= i:
                return (i , nums.index(result))
                 