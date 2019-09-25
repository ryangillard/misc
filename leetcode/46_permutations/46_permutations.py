import itertools

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = []
        self.recursive(nums, [], perms)
        return perms

    def recursive(self, nums, perm, perms):
        if len(nums) == 0:
            perms.append(perm)

            return None

        for i in range(len(nums)):
            self.recursive(nums[:i] + nums[i + 1:], perm + [nums[i]], perms)

        return None