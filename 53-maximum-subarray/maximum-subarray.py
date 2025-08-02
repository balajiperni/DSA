class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        max_number = nums[0]

        for i in range(1 , len(nums)):
            max_number = max(nums[i] , max_number + nums[i])
            result = max(result ,  max_number)
        return result    
        