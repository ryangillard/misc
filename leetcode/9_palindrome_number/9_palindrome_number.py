class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return self.intMethod(x)

    def stringMethod(self, x):
        return str(x) == str(x)[::-1]

    def intMethod(self, x):
        # Negatives can't be, also anything perfectly divisible by powers of 10, except 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Extract first half of digits
        reverted_number = 0
        while x > reverted_number:
            # Expand reverted number back out and add remainder
            reverted_number = reverted_number * 10 + x % 10
            x /= 10
        
        # Return for even or odd sequences
        return x == reverted_number or x == reverted_number / 10