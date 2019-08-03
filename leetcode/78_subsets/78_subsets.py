class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sub = []
        output = [[]]
        output = self.helper(nums, sub, output)

        return output

    def helper(self, nums, sub, output):
        for i, num in enumerate(nums):
            output.append(sub + [num])
            output = self.helper(nums=nums[i + 1:], sub=sub + [num], output=output)

        return output