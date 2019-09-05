class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.singleHashMap(s, t)

    def doubleHashMap(self, s, t):
        s_hashmap = self.createHashmap(s)
        t_hashmap = self.createHashmap(t)

        if len(s_hashmap) != len(t_hashmap):
            return False

        for key in s_hashmap.keys():
            if key in t_hashmap:
                if s_hashmap[key] != t_hashmap[key]:
                    return False
            else:
                return False

        return True

    def createHashmap(self, s):
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.setdefault(c, 0) + 1

        return hashmap

    def singleHashMap(self, s, t):
        hashmap = {}

        for c in s:
            hashmap[c] = hashmap.setdefault(c, 0) + 1

        for c in t:
            hashmap[c] = hashmap.setdefault(c, 0) - 1

        return all([x == 0 for x in hashmap.values()])