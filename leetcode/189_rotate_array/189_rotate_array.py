class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums_copy = nums[:]
        nums_copy = nums_copy[-k:] + nums_copy[:-k]
        for i in range(len(nums)):
            nums[i] = nums_copy[i]

        return None