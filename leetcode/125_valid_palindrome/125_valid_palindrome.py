class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([c for c in s if c.isalnum()]).lower()
        length = len(s)
        return s[:length // 2] == (s[length // 2:][::-1] if length % 2 == 0 else s[length // 2 + 1:][::-1])