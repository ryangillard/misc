class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counts1 = self.calcCounts(nums1)
        counts2 = self.calcCounts(nums2)

        intersection = set(counts1.keys()) & set(counts2.keys())

        ret = []
        for num in intersection:
            ret.extend([num] * min(counts1[num], counts2[num]))

        return ret

    def calcCounts(self, nums):
        counts = {}
        for num in nums:
            counts[num] = counts.setdefault(num, 0) + 1

        return counts