class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        elif num == 1:
            return True

        while num % 4 == 0:
            num //= 4

        return num == 1