class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Quick exit
        if not matrix:
            return False
        if not matrix[0]:
            return False
        
        return self.singleBinarySearch(matrix, target)
    
    def singleBinarySearch(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        lo = 0
        hi = rows * cols - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False

    def doubleBinarySearch(self, matrix, target):
        # Search rows
        row_idx, found = self.rowBinarySearch(matrix, target)
        if found:
            return True
        elif row_idx < 0:
            return False

        # Search columns
        return self.colBinarySearch(matrix, target, row_idx)

    def rowBinarySearch(self, matrix, target):
        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] == target:
                return mid, True
            elif matrix[mid][0] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo - 1, False

    def colBinarySearch(self, matrix, target, row_idx):
        lo = 0
        hi = len(matrix[row_idx]) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[row_idx][mid] == target:
                return True
            elif matrix[row_idx][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False