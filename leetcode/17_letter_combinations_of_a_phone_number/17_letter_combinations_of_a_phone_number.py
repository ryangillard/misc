class Solution(object):
    import itertools
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        num_letter_map = {"2": ["a", "b", "c"],
                          "3": ["d", "e", "f"],
                          "4": ["g", "h", "i"],
                          "5": ["j", "k", "l"],
                          "6": ["m", "n", "o"],
                          "7": ["p", "q", "r", "s"],
                          "8": ["t", "u", "v"],
                          "9": ["w", "x", "y", "z"]}

        letter_lists = []
        for digit in digits:
            letter_lists.append(num_letter_map[digit])

        permutations = itertools.product(*letter_lists)

        return ["".join(perm) for perm in permutations]