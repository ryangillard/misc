class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.setdefault(num, 0) + 1

        max_value = -sys.maxint
        majority_element = None
        for num in hashmap.keys():
            if hashmap[num] > max_value:
                max_value = hashmap[num]
                majority_element = num

        return majority_element