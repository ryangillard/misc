class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        full_length = len(nums) + 1

        for num in range(full_length):
            if num not in nums_set:
                return num