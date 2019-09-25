class Solution(object):
    def __init__(self):
        self.count = 0

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.dp_bottom_up(sorted(nums), target)
        return self.count

    def recursive(self, nums, target):
        if target == 0:
            self.count += 1

            return None

        for i in range(len(nums)):
            if nums[i] > target:
                break

            self.recursive(nums, target - nums[i])

        return None

    def dp_bottom_up(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]

        self.count = dp[target]

        return None