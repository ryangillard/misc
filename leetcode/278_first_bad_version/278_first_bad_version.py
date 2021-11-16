# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n - 1
        while left <= right:
            index = left + (right - left) // 2
            if isBadVersion(version=index + 1):
                right = index - 1
            else:
                left = index + 1
        return left + 1