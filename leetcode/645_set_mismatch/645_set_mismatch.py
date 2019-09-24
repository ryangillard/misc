class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.fast(nums)

    def slow(self, nums):
        # Find duplicate
        count = {}
        for num in nums:
            count[num] = count.setdefault(num, 0) + 1
            if count[num] > 1:
                duplicate = num

        # Find missing
        nums_set = set(nums)
        full_set = set([i for i in range(1, len(nums) + 1)])
        missing = full_set - nums_set

        return [duplicate] + list(missing)

    def medium(self, nums):
        # Find duplicate
        count = {}
        for num in nums:
            count[num] = count.setdefault(num, 0) + 1
            if count[num] > 1:
                duplicate = num

        # Find missing
        nums_set = set(count.keys())
        full_set = set([i for i in range(1, len(nums) + 1)])
        missing = full_set - nums_set

        return [duplicate] + list(missing)

    def fast(self, nums):
        # Find duplicate
        count = {}
        for num in nums:
            count[num] = count.setdefault(num, 0) + 1
            if count[num] > 1:
                duplicate = num
                break

        # Find missing
        # nums_set = set(count.keys())
        nums_set = set(nums)
        full_set = set([i for i in range(1, len(nums) + 1)])
        missing = full_set - nums_set

        return [duplicate] + list(missing)