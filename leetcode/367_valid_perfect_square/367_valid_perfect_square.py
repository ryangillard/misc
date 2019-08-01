class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = self.binarySearch(num)
        return True if x * x == num else False

    def binarySearch(self, num):
        if num == 0:
            return 0

        lo = 0
        hi = num / 2 + 1
        while lo <= hi:
            mid = lo + (hi - lo) / 2

            prod = mid ** 2
            
            if prod == num:
                return mid
            elif prod < num:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return lo + (hi - lo) / 2