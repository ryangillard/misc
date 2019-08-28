class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        nmin = min(n1, n2)
        nmax = max(n1, n2)
        sum_list = [0] * nmax

        i = 0

        carry = 0
        while i< nmin:
            i, carry, sum_list = self.addList(int(num1[~i]) + int(num2[~i]) + carry, i, carry, sum_list)

        if n1 > n2:
            while i< n1:
                i, carry, sum_list = self.addList(int(num1[~i]) + carry, i, carry, sum_list)
        else:
            while i< n2:
                i, carry, sum_list = self.addList(int(num2[~i]) + carry, i, carry, sum_list)

        if carry:
            print(sum_list)
            print(sum_list[-1])
            if sum_list[-1] == "9":
                sum_list[-1] = "0"
            sum_list.append("1")

        return "".join([str(x) for x in sum_list[::-1]])

    def addList(self, summed, i, carry, sum_list):
        add = summed % 10
        sum_list[i] = add
        carry = 1 if summed > 9 else 0
        i += 1

        return i, carry, sum_list