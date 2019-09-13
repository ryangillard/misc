class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(nums)

        if len(hashset) < 3:
            return max(hashset)

        hashset.remove(max(hashset))
        hashset.remove(max(hashset))

        return max(hashset)