class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # Find max exponent
        base = max(x, y) if x == 1 or y == 1 else min(x, y)
        exponent = 1
        if base != 1:
            while base ** exponent <= bound:
                exponent += 1

        # Brute force all of the exponent trials
        hashset = set()
        for i in range(exponent):
            for j in range(exponent):
                z = x ** i + y ** j

                if z <= bound:
                    hashset.add(z)

        return list(hashset)