class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.oneExplicitLoopLessMemory(nums)

    def threeLoops(self, nums):
        if nums:
            left = [0] * len(nums)
            right = [0] * len(nums)

            right[-1] = nums[-1]
            for i in range(len(nums) - 2, -1, -1):
                right[i] = right[i + 1] + nums[i]

            left[0] = nums[0]
            for i in range(1, len(nums)):
                left[i] = left[i - 1] + nums[i]

            for i in range(len(nums)):
                if left[i] == right[i]:
                    return i

        return -1

    def twoLoops(self, nums):
        if nums:
            left = [0] * len(nums)
            right = [0] * len(nums)

            right[-1] = nums[-1]
            for i in range(len(nums) - 2, -1, -1):
                right[i] = right[i + 1] + nums[i]

            left[0] = nums[0]
            if left[0] == right[0]:
                return i

            for i in range(1, len(nums)):
                left[i] = left[i - 1] + nums[i]
                if left[i] == right[i]:
                    return i

        return -1

    def oneExplicitLoopLessMemory(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1