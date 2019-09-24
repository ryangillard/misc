class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nums = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        num_str = []
        found_sign = False
        found_num = False
        for i in range(len(str)):
            if str[i] in nums:
                num_str.append(str[i])
                found_num = True
            else:
                if found_num:
                    return self.finished(num_str)
                else:
                    if str[i] == "+":
                        if found_sign:
                            return 0
                        else:
                            num_str.append(str[i])
                            found_sign = True
                    elif str[i] == "-":
                        if found_sign:
                            return 0
                        else:
                            num_str.append(str[i])
                            found_sign = True
                    elif str[i] == " ":
                        if found_sign or found_num:
                            return 0
                        else:
                            continue
                    else:
                        return 0

        if found_num:
            return self.finished(num_str)
        else:
            return 0

    def finished(self, num_str):
        if num_str[0] == "+":
            num = int("".join(num_str[1:]))
            return min(num, 2 ** 31 - 1)
        elif num_str[0] == "-":
            num = int("".join(num_str))
            return max(num, -2 ** 31)
        else:
            num = int("".join(num_str))
            return min(num, 2 ** 31 - 1)