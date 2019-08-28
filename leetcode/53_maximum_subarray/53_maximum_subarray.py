class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = -sys.maxint - 1
        largest_sum = 0
        subarray_sum = 0

        for i in range(len(nums)):
            subarray_sum += nums[i]
            
            if subarray_sum <= 0:
                subarray_sum = 0

            if nums[i] > max_num:
                max_num = nums[i]
                
            largest_sum = max(largest_sum, subarray_sum)

        if largest_sum == 0:
            largest_sum = max_num

        return largest_sum