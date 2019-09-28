class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.hashmap(nums, target)

    def naive(self, nums, target):
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def hashmap(self, nums, target):
        hashmap = dict()
        for i in range(len(nums)):
            hashmap[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in hashmap:
                if i != hashmap[nums[i]]:
                    return [i, hashmap[nums[i]]]