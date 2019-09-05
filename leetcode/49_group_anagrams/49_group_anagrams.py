class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # General for any characters
        vocab_idx_dict = {c: i for i, c in enumerate(set("".join(strs)))}

        hashmap = {}
        for s in strs:
            counts = [0] * len(vocab_idx_dict)
            for c in s:
                counts[vocab_idx_dict[c]] += 1

            key = tuple(counts)
            if hashmap.get(key):
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]

        return hashmap.values()