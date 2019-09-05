class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        self.backward(nums1, m, nums2, n) 

        return None

    def forward(self, nums1, m, nums2, n):
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

        return None
    
    def backward(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        idx = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1

        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1

        return None