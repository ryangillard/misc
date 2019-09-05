class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.setdefault(num, 0) + 1

        majority_elements = []
        for num in hashmap.keys():
            if hashmap[num] > len(nums) // 3:
                majority_elements.append(num)

        return majority_elements