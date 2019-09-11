class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = 0

        while target > 0:
            k += 1
            target -=k

        if target % 2 == 0:  # even
            return k
        return k + 1 + k % 2  # odd