class Solution(object):
    def __init__(self):
        self.INT_MIN = -2 ** 31
        self.INT_MAX = -self.INT_MIN - 1

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.modAdd(x)

    def trivial(self, x):
        neg = False
        if x < 0:
            neg = True
            x = -x

        xs = str(x)
        xsr = xs[::-1]
        xi = int(xsr)

        if neg:
            if xi > -self.INT_MIN:
                xi = 0
            else:
                xi = -xi
        else:
            if xi > self.INT_MAX:
                xi = 0

        return xi

    def modAdd(self, x):
        reverse = 0
        neg = False
        if x < 0:
            neg = True
            x = -x

        while x != 0:
            # Get last digit
            digit = x % 10

            # Remove last digit
            x /= 10

            # Check for overflow for positive x
            if reverse > self.INT_MAX / 10 or (reverse == self.INT_MAX / 10 and digit > 7):
                return 0

            # Check for overflow for negative x
            if neg and (reverse > -self.INT_MIN / 10 or (reverse == -self.INT_MIN / 10 and digit > 7)):
                return 0

            # Add last digit to reverse
            reverse = reverse * 10 + digit

        if neg:
            reverse = -reverse

        return reverse