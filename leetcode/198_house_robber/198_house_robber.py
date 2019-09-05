class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.trackers(nums)

    def dynamicProgramming(self, nums):
        # Quick exits
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # Make dp array
        dp = [0] * len(nums)

        # Initialize starting values
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Loop through the rest and update dp
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

    def trackers(self, nums):
        single_jump = 0
        double_jump = 0

        for i in range(len(nums)):

            temp = single_jump
            single_jump = double_jump
            double_jump = max(nums[i] + temp, double_jump)

        return double_jump