class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_note_counter = self._counter({}, ransomNote)
        magazine_counter = self._counter({}, magazine)

        if len(ransom_note_counter) > len(magazine_counter):
            return False

        ransom_note_chars = ransom_note_counter.keys()
        magazine_chars = magazine_counter.keys()

        for c in ransom_note_chars:
            if c not in magazine_chars:
                return False

            if ransom_note_counter[c] > magazine_counter[c]:
                return False

        return True
        
    def _counter(self, counter, string):
        for c in string:
            counter[c] = counter.setdefault(c, 0) + 1

        return counter