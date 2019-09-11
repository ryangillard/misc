class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        elif num == 1:
            return True

        number = num
        factors = []
        i = 2
        while i <= 5 and number > 1:
            if number % i == 0:
                number /= i
            else:
                 i += 1

        return number <= 1