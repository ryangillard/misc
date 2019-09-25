class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.noExtraSpace(nums)

    def extraSpace(self, nums):
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.setdefault(nums[i], 0) + 1

        return [num for num in count.keys() if count[num] > 1]

    def noExtraSpace(self, nums):
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -nums[idx]

        return [i + 1 for i in range(len(nums)) if nums[i] < 0]