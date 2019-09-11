class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_set = set(banned)
        paragraph_word_count = dict()
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        for word in paragraph.lower().split():
            paragraph_word_count[word] = paragraph_word_count.setdefault(word, 0) + 1

        max_count = 0
        max_word = ""
        for word in paragraph_word_count:
            if word not in banned_set:
                if paragraph_word_count[word] > max_count:
                    max_count = paragraph_word_count[word]
                    max_word = word

        return max_word