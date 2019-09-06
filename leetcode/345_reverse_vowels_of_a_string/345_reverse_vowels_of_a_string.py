class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        left = 0
        right = len(s) - 1
        
        return self.listMethod(s, left, right, vowels)

    def listMethod(self, s, left, right, vowels):
        s = [c for c in s]
        while left < right:
            if s[left] in vowels:
                if s[right] in vowels:
                    temp = s[left]
                    s[left] = s[right]
                    s[right] = temp
                    left += 1
                right -= 1
            else:
                if not s[right] in vowels:
                    right -= 1
                left += 1

        return "".join(s)

    def stringMethod(self, s, left, right, vowels):
        while left < right:
            if s[left] in vowels:
                if s[right] in vowels:
                    s = s[:left] + s[right] + s[left + 1:right] + s[left] + s[right + 1:]
                    left += 1
                right -= 1
            else:
                if not s[right] in vowels:
                    right -= 1
                left += 1

        return "".join(s)