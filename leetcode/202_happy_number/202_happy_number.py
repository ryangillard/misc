class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # The smallest happy number after 1 is 7
        while n > 6:
            # Split n into a list of squared digits
            squared_digits = [int(x) ** 2 for x in str(n)]

            # Recurse now with new sum
            return self.isHappy(sum(squared_digits))

        # The smallest happy number is 1, so return that if we've gotten this far
        return True if n == 1 else False