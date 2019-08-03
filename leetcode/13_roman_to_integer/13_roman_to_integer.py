class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        singles = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        subtractions = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        i = 0
        sum = 0

        if len(s) == 1:
            return singles[s[0]]

        while i < len(s) - 1:
            if s[i] + s[i + 1] in subtractions:
                sum += subtractions[s[i] + s[i + 1]]
                i += 2
            else:
                sum += singles[s[i]]
                i += 1

        if s[-2] + s[-1] not in subtractions:
            sum += singles[s[-1]]

        return sum