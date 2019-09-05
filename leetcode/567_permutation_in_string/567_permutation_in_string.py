class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Quick return
        if not s2 or not s1 or len(s2) < len(s1):
            return False

        # Create hashmap for string s1 of character counts
        s1_hashmap = {}
        for c in s1:
            s1_hashmap[c] = s1_hashmap.setdefault(c, 0) + 1

        # Initialize hashmap for substring s2 of character counts
        s2_hashmap = {}
        for i in range(len(s1)):
            c = s2[i]
            s2_hashmap[c] = s2_hashmap.setdefault(c, 0) + 1

        # Initialize valid_anagram
        valid_anagram = self.validAnagram(s2_hashmap, s1_hashmap)
        if valid_anagram:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            old_c = s2[i - 1]
            new_c = s2[i - 1 + len(s1)]

            # If previous subsequence was NOT a valid anagram, see if new character flips that
            if old_c != new_c:
                s2_hashmap[old_c] -= 1
                if s2_hashmap[old_c] == 0:
                    del s2_hashmap[old_c]
                s2_hashmap[new_c] = s2_hashmap.setdefault(new_c, 0) + 1

                valid_anagram = self.validAnagram(s2_hashmap, s1_hashmap)
                if valid_anagram:
                    return True

        return False

    def validAnagram(self, s2_hashmap, s1_hashmap):
        if len(s2_hashmap) != len(s1_hashmap):
            return False

        for key in s1_hashmap:
            if key in s2_hashmap:
                if s2_hashmap[key] != s1_hashmap[key]:
                    return False
            else:
                return False

        return True