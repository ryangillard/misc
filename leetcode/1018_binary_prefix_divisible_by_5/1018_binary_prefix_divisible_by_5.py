class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        return self.prefixMod(A)

    def forLoop(self, A):
        A = "".join([str(x) for x in A])
        ret = [False] * len(A)
        for i in range(len(A)):
            if int(A[:i + 1], 2) % 5 == 0:
                ret[i] = True

        return ret

    def listComp(self, A):
        A = "".join([str(x) for x in A])

        return [int(A[:i + 1], 2) % 5 == 0 for i in range(len(A))]

    def prefixMod(self, A):
        for i in range(1, len(A)):
            A[i] += (A[i - 1] * 2) % 5

        return [x % 5 == 0 for x in A]