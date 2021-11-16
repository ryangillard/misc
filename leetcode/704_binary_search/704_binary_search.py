class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            index = left + (right - left) // 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                right = index - 1
            else:
                left = index + 1
        return -1