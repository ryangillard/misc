class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.hashMap(nums, k)

    def cumSum(self, nums, k):
        count = 0
        cum_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            cum_sum[i] = cum_sum[i - 1] + nums[i - 1]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if cum_sum[j] - cum_sum[i] == k:
                    count += 1

        return count
    
    def cumSumNoSpace(self, nums, k):
        count = 0
        for i in range(len(nums)):
            cum_sum = 0
            for j in range(i, len(nums)):
                cum_sum += nums[j]
                if cum_sum == k:
                    count += 1

        return count

    def hashMap(self, nums, k):
        count = 0
        cum_sum = 0
        hashmap = {0: 1}

        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum - k in hashmap:
                count += hashmap[cum_sum - k]

            hashmap[cum_sum] = hashmap.setdefault(cum_sum, 0) + 1

        return count