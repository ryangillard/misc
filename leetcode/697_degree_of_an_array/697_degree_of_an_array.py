class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create hashmap of instance counts of each unique number
        leftmost = {}
        rightmost = {}
        instance_counts = {}
        
        for i, num in enumerate(nums):
            if num not in leftmost:
                leftmost[num] = i
            rightmost[num] = i
            instance_counts[num] = instance_counts.setdefault(num, 0) + 1
                
        # Find degree of nums
        degree = max(instance_counts.values())
        
        # Find min length
        min_len = len(nums)
        
        for num in instance_counts:
            if instance_counts[num] == degree:
                min_len = min(min_len, rightmost[num] - leftmost[num] + 1)

        return min_len