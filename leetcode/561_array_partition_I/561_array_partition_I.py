class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort to get them in order and take the even elements which will be the minimums
        return sum(sorted(nums)[::2])