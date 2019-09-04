class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        total_len = m + n
        while i < m and j < n:
            if nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                del nums1[-1]
                m += 1
                j += 1
            else:
                i += 1

        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1