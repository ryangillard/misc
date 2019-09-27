class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.noDivision(nums)

    def division(self, nums):
        prod = 1
        for num in nums:
            prod *= num

        return [0 if num == 0 else prod / num for num in nums]

    def noDivision(self, nums):
        outputs = [1] * len(nums)
        for i in range(1, len(nums)):
            outputs[i] = outputs[i - 1] * nums[i - 1]

        right = 1
        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            outputs[i] *= right

        return outputs