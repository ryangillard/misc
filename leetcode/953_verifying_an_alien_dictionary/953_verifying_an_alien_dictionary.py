class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_dict = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    if order_dict[words[i][j]] > order_dict[words[i + 1][j]]:
                        return False
                    break
                else:
                    if len(words[i]) > len(words[i + 1]):
                        return False

        return True