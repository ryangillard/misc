class Solution(object):
    def sortArrayByParity(self, A):
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

        return evens + odds