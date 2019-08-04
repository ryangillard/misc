class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums

        flat = [col for row in nums for col in row]

        return [flat[i * c:(i + 1) * c] for i in range(r)]