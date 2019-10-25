class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        singles = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
        teens = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"}
        tens = {"2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"}
        powers_of_three_list = ["", "Thousand", "Million", "Billion"]

        nums = str(num)
        english = []
        i = len(nums) - 1
        digit = 0
        while i >= 0:
            if digit % 3 == 0:
                if digit >= 3:
                    if not english or english[-1] != powers_of_three_list[digit // 3 - 1]:
                        english.append(powers_of_three_list[digit // 3])
                    else:
                        english[-1] = powers_of_three_list[digit // 3]

                if i > 0 and nums[i - 1] == "1":
                    english.append(teens[nums[i-1:i+1]])
                    i -= 1
                    digit += 1
                elif nums[i] != "0":
                    english.append(singles[nums[i]])
            elif digit % 3 == 1:
                if nums[i] != "1" and nums[i] != "0":
                    english.append(tens[nums[i]])
            elif digit % 3 == 2:
                if nums[i] != "0":
                    english.extend(["Hundred", singles[nums[i]]])

            i -= 1
            digit += 1

        return " ".join(english[::-1])