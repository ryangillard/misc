class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        perms = []
        perm = []
        open = 0
        closed = 0

        perms = self.add_perm(n, open, closed, perm, perms)

        return perms

    def add_perm(self, n, open, closed, perm, perms):
        if len(perm) == 2 * n:
            perms.append("".join(perm))
            return perms

        if open < n:
            perms = self.add_perm(n, open + 1, closed, perm + ["("], perms)

        if closed < n and open > closed:
            perms = self.add_perm(n, open, closed + 1, perm + [")"], perms)

        return perms