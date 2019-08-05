class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        counts = {"U": 0, "D": 0, "L": 0, "R": 0}
        for move in moves:
            counts[move] += 1
        return counts["U"] == counts["D"] and counts["L"] == counts["R"]