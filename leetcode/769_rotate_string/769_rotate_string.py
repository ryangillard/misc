class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A:
            if not B:
                return True
            else:
                return False
        elif not B:
            return False

        for _ in range(len(A) - 1):
            A = A[1:] + A[0]

            if A == B:
                return True

        return False