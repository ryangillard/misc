class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = []
        roman = self.generalCase(num, roman)
        
        return roman

    def generalCase(self, num, roman):
        combined_rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV"]
        combined_int = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4]

        while num > 0:
            if num == 1:
                roman.append("I")
                num = 0
            elif num == 2:
                roman.append("II")
                num = 0
            elif num == 3:
                roman.append("III")
                num = 0
            else:
                for i in range(len(combined_int)):
                    if num - combined_int[i] >= 0:
                        roman.append(combined_rom[i])
                        num -= combined_int[i]
                        break

        return "".join(roman)