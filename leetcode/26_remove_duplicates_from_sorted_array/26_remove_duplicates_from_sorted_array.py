class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = self.usingPtrsFor(nums)

        return length

    def usingDel(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
            else:
                i += 1
        return len(nums)

    def usingPtrsWhile(self, nums):
        if len(nums) == 0:
            return 0

        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1

    def usingPtrsFor(self, nums):
        if len(nums) == 0:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1