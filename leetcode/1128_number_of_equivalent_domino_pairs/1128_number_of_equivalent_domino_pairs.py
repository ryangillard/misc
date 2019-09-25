class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        hashmap = dict()
        for a, b in dominoes:
            key = tuple([min(a, b), max(a, b)])
            hashmap[key] = hashmap.setdefault(key, 0) + 1

        count = 0
        for v in hashmap.values():
            count += v * (v - 1)

        return count // 2