class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = dict()
        left_idx = 0
        right_idx = -1
        max_len = 0
        for right_idx in range(len(s)):
            if s[right_idx] in hashmap:
                shift_idx = hashmap[s[right_idx]] + 1
                max_len = max(max_len, right_idx - left_idx)
                if shift_idx > left_idx:
                    left_idx = shift_idx
            hashmap[s[right_idx]] = right_idx

        max_len = max(max_len, right_idx - left_idx + 1)

        return max_len