class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = s.split(" ")
        strs = [list(st) for st in strs]

        return self.noFancyListStuff(s)

    def noFancyListStuff(self, s):
        s = list(s)
        start_of_string = 0
        end_of_string = 0
        while end_of_string < len(s):
            if s[end_of_string] == " " or end_of_string == len(s) - 1:
                i = start_of_string
                j = end_of_string - 1 if s[end_of_string] == " " else len(s) - 1
                while i < j:
                    temp = s[i]
                    s[i] = s[j]
                    s[j] = temp
                    i += 1
                    j -= 1
                start_of_string = end_of_string + 1
            end_of_string += 1

        return "".join(s)

    def fancyListStuff(self, strs):
        for i in range(len(strs)):
            strs[i] = "".join(strs[i][::-1])

        return " ".join(strs)