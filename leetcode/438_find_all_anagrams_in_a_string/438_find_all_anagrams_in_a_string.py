class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        anagram_indices = []

        # Quick return
        if not s or not p or len(s) < len(p):
            return anagram_indices

        # Create hashmap for string p of character counts
        p_hashmap = {}
        for c in p:
            p_hashmap[c] = p_hashmap.setdefault(c, 0) + 1

        # Initialize hashmap for substring s of character counts
        s_hashmap = {}
        for i in range(len(p)):
            c = s[i]
            s_hashmap[c] = s_hashmap.setdefault(c, 0) + 1

        # Initialize valid_anagram
        valid_anagram = self.validAnagram(s_hashmap, p_hashmap)
        if valid_anagram:
            anagram_indices.append(0)

        for i in range(1, len(s) - len(p) + 1):
            old_c = s[i - 1]
            new_c = s[i - 1 + len(p)]

            if valid_anagram:
                # If previous subsequence was already a valid anagram, just check to see if character changed
                if old_c == new_c:
                    anagram_indices.append(i)
                else:
                    valid_anagram = False

                    s_hashmap[old_c] -= 1
                    s_hashmap[new_c] = s_hashmap.setdefault(new_c, 0) + 1
            else:
                # If previous subsequence was NOT a valid anagram, see if new character flips that
                if old_c != new_c:
                    s_hashmap[old_c] -= 1
                    if s_hashmap[old_c] == 0:
                        del s_hashmap[old_c]
                    s_hashmap[new_c] = s_hashmap.setdefault(new_c, 0) + 1

                    valid_anagram = self.validAnagram(s_hashmap, p_hashmap)
                    if valid_anagram:
                        anagram_indices.append(i)

        return anagram_indices

    def validAnagram(self, s_hashmap, p_hashmap):
        if len(s_hashmap) != len(p_hashmap):
            return False

        for key in p_hashmap:
            if key in s_hashmap:
                if s_hashmap[key] != p_hashmap[key]:
                    return False
            else:
                return False

        return True