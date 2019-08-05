class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.checkEndsMethod(s)

    def bruteForceMethod(self, s):
        length = len(s)

        # Quick return if length 1
        if length == 1:
            return True

        # Check if string is already palindrome
        if self.validatePalindrome(s, length):
            return True

        # Iterate through string temporarily removing a character at a time and check
        for i in range(length - 1):
            if self.validatePalindrome(s[:i] + s[i + 1:], length - 1):
                return True

        # Temporarily remove final character and check
        if self.validatePalindrome(s[:-1], length - 1):
            return True
        else:
            return False

    def checkEndsMethod(self, s):
        length = len(s)

        # Quick return if length 1
        if length == 1:
            return True

        # Check if string is already palindrome
        if self.validatePalindrome(s, length):
            return True

        # Iterate through string from both ends toward the middle and check
        for i in range(length // 2):
            # If ends are different, make the change and validate
            if s[i] != s[-(i + 1)]:
                # Temporarily remove front character and check
                remove_front = self.validatePalindrome(s[i + 1:length - i], length - 1 - 2 * i)
                # Temporarily remove back character and check
                remove_back = self.validatePalindrome(s[i:-(i + 1)], length - 1 - 2 * i)

                return (remove_front or remove_back)

    def validatePalindrome(self, s, length):
        return s[:length // 2] == (s[length // 2:][::-1] if length % 2 == 0 else s[length // 2 + 1:][::-1])