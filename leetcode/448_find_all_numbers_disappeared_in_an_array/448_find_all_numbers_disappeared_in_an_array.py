class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.noExtraSpace(nums)

    def extraSpace(self, nums):
        found = [False] * len(nums)
        for i in range(len(nums)):
            found[nums[i] - 1] = True

        return [i + 1 for i in range(len(found)) if not found[i]]

    def noExtraSpace(self, nums):
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]