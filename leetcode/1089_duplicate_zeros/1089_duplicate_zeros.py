class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Count zeros
        num_zeros = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                num_zeros += 1

        if num_zeros == 0:
            return arr

        # Rebuild array in place backwards
        i = len(arr) - 1
        while i >= 0 and num_zeros > 0:
            if i + num_zeros < len(arr):
                arr[i + num_zeros] = arr[i]
            if arr[i] == 0:
                num_zeros -= 1
                if i + num_zeros < len(arr):
                    arr[i + num_zeros] = 0
            i -= 1

        return None