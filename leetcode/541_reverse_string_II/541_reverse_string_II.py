class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)

        return self.fancyListStuff(s, k)

    def noFancyListStuff(self, s, k):
        for p in range(0, len(s), 2 * k):
            # i and j are swap indices sliding right and left respectively within each 2k window
            i = p
            j = min(p + k - 1, len(s) - 1)
            while i < j:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1

        return "".join(s)

    def fancyListStuff(self, s, k):
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = s[i:i + k][::-1]

        return "".join(s)