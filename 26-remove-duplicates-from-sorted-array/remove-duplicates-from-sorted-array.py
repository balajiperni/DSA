class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
                result.append(num)

        # Modify nums in-place
        for i in range(len(result)):
            nums[i] = result[i]

        return len(result)
