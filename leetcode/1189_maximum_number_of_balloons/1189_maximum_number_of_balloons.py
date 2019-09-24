class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        valid_chars = set(["b", "a", "l", "o", "n"])

        # Count valid character occurrences
        counts = {k: 0 for k in valid_chars}
        for c in text:
            if c in valid_chars:
                counts[c] += 1

        print(counts)

        # Find min count
        min_count = min(counts.values())

        # Check if there are enough l's and o's
        return min(min_count, min(counts["l"] // 2, counts["o"] // 2))