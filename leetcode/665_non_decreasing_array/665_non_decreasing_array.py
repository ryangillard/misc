class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                if count > 1:
                    return False

                ret_left = self.checkLeft(i, nums)
                ret_self = self.checkSelf(i, nums)

                if not ret_left and not ret_self:
                    return False

        if count <= 1:
            return True

    def checkLeft(self, drop_index, nums):
        count = 0
        for i in range(drop_index - 1, -1, -1):
            if nums[i] > nums[drop_index]:
                count += 1
                if count > 1:
                    return False

        if count == 1:
            return True

    def checkSelf(self, drop_index, nums):
        if drop_index == len(nums) - 1:
            return True

        left = nums[drop_index - 1]
        right = nums[drop_index + 1]

        if left <= right:
            return True

        return False