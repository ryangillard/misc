class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.binarySearch(x)

    def trivial(self, x):
        return int(x**0.5)
    
    def brute(self, x):
        if x == 0:
            return 0

        i = 1
        while True:
            if i * i > x:
                return i - 1

            i += 1

    def binarySearch(self, x):
        if x == 0:
            return 0

        lo = 0
        hi = x / 2 + 1
        while lo <= hi:
            mid = lo + (hi - lo) / 2

            prod = mid ** 2
            
            if prod == x:
                return mid
            elif prod < x:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return lo + (hi - lo) / 2