class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = self.usingPtrsFor(nums, val)

        return length

    def usingDel(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)

    def usingPtrsWhile(self, nums, val):
        if len(nums) == 0:
            return 0

        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

    def usingPtrsFor(self, nums, val):
        if len(nums) == 0:
            return 0

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow