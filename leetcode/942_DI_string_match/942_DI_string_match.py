class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        inc = 0
        dec = len(S)

        perm = []
        for i in range(len(S)):
            if S[i] == "I":
                perm.append(inc)
                inc +=1
            else:
                perm.append(dec)
                dec -= 1

        return perm + [dec]