class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        substring = []
        substrings = []
        self.recursive(s, substring, substrings)

        return substrings

    def recursive(self, s, substring, substrings):
        if not s:
            substrings.append(substring)

            return None

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[0:i]):
                self.recursive(s[i:len(s)], substring + [s[0:i]], substrings)

    def isPalindrome(self, s):
        return s == s[::-1]