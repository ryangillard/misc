class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        # O(n) time, O(1) memory
        return self.stackMethod(S)

    def pointerMethod(self, S):
        p = 0
        while p < len(S) - 1:
            if S[p] == S[p + 1]:
                S = S[:p] + S[p + 2:] if len(S) > 2 else ""
                p = p - 1 if p > 0 else p
            else:
                p += 1

        return S

    def stackMethod(self, S):
        stack = []

        for s in S:
            if not stack or s != stack[-1]:
                stack.append(s)
            else:
                stack.pop()

        return "".join(stack)