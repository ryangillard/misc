class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Find decreasing element
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[i - 1]:
                break

        # Find swap point
        if i - 1 >= 0:
            for j in range(i, len(nums)):
                if j + 1 < len(nums) and nums[j + 1] <= nums[i - 1]:
                    break

            # Swap two numbers
            self.swap(i - 1, j, nums)

        # Reverse end sequence
        for k in range((len(nums) - i) // 2):
            left = i + k
            right = len(nums) - 1 - k
            self.swap(left, right, nums)

        return nums

    def swap(self, i, j, nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

        return None