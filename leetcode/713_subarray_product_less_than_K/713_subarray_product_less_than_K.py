class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        product = 1
        count = 0
        left = 0
        right = 0

        while right < len(nums):
            # Keep going right
            product *= nums[right]

            # If we overshoot k, start chopping off left
            while product >= k:
                product /= nums[left]
                left += 1

            # Accounts for subarrays within subarray that we didn't explicitly try
            count += right - left + 1

            right += 1

        return count