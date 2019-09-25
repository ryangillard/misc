class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = set()
        self.recursive(nums, [], perms)

        return perms

    def recursive(self, nums, perm, perms):
        if len(nums) == 0:
            perms.add(tuple(perm))

            return None

        for i in range(len(nums)):
            self.recursive(nums[:i] + nums[i + 1:], perm + [nums[i]], perms)

        return None