class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        idx = self.naiveCharFor(haystack, needle)

        return idx

    def naiveCharWhile(self, haystack, needle):
        if not needle or haystack == needle:
            return 0
        
        slow = 0
        while slow < len(haystack) - len(needle) + 1:
            if haystack[slow] == needle[0]:
                count = 1
                for fast, char in enumerate(needle[1:]):
                    if slow + 1 + fast < len(haystack) and haystack[slow + 1 + fast] == char:
                        count += 1
                    else:
                        break

                if count == len(needle):
                    return slow
            slow += 1

        return -1

    def naiveCharFor(self, haystack, needle):
        if not needle or haystack == needle:
            return 0
        
        for slow in range(len(haystack) - len(needle) + 1):
            if haystack[slow] == needle[0]:
                count = 1
                for fast, char in enumerate(needle[1:]):
                    if slow + 1 + fast < len(haystack) and haystack[slow + 1 + fast] == char:
                        count += 1
                    else:
                        break

                if count == len(needle):
                    return slow

        return -1
        