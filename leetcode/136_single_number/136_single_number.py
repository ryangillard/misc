class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.hashtable_try_except(nums, {})

    def hashtable_if_else(self, nums, hashtable):
        for num in nums:
            if num in list(hashtable):
                hashtable.pop(num)
            else:
                hashtable[num] = 1

        return list(hashtable)[0]

    def hashtable_try_except(self, nums, hashtable):
        for num in nums:
            try:
                hashtable.pop(num)
            except:
                hashtable[num] = 1

        return list(hashtable)[0]