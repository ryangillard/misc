class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # Reverse each row
        for row in A:
            self.reverse(row)

        # Invert entire matrix
        self.invert(A)

        return A

    def reverse(self, row):
        for i in range(len(row) // 2):
            left = i
            right = len(row) - 1 - i

            self.swap(left, right, row)

        return None

    def swap(self, i, j, row):
        temp = row[i]
        row[i] = row[j]
        row[j] = temp

        return None

    def invert(self, A):
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = 1 - A[i][j]

        return None