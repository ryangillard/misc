class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.one_pointer(s)

    def one_pointer(self, s):
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[~i]
            s[~i] = temp

    def two_pointer(self, s):
        left, right = 0, len(s) - 1
        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1