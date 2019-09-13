class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashset = set()
        hashmap = dict()
        for i in range(len(s)):
            if hashmap.get(s[i]) is None:
                hashmap[s[i]] = i
                hashset.add(s[i])
            else:
                if s[i] in hashset:
                    hashset.remove(s[i])

        min_idx = sys.maxint
        for c in hashset:
            if hashmap[c] < min_idx:
                min_idx = hashmap[c]

        return min_idx if min_idx < sys.maxint else -1