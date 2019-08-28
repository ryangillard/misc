class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evens = []
        odds = []

        for element in A:
            if element % 2 == 0:
                evens.append(element)
            else:
                odds.append(element)

        ret = [0] * len(A)
        for i in range(len(evens)):
            ret[2 * i] = evens[i]
            ret[2 * i + 1] = odds[i]

        return ret