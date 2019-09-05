class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.hashsetMethod(nums)

    def hashmapMethod(self, nums):
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.setdefault(num, 0) + 1
            if hashmap[num] > 1:
                return True

        return False

    def hashsetMethod(self, nums):
        return len(set(nums)) < len(nums)