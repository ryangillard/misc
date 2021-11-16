class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.slow_fast(nums)

    def pop_append(self, nums):
        i = 0
        zero_start = len(nums)

        while i < len(nums) and zero_start >= 0:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                zero_start -= 1
            else:
                i += 1

    def slow_fast(self, nums):
        slow, fast = 0, 0

        while slow <= fast and fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while slow < len(nums):
            nums[slow] = 0
            slow += 1
