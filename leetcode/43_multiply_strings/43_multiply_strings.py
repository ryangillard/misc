class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return self.allowedMethod(num1, num2)

    def cheatMethod(self, num1, num2):
        return str(int(num1) * int(num2))

    def bigintMethod(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)
        product = 0
        for i in range(n1):
            int1 = int(num1[i]) * 10 ** (n1 - 1 - i)
            for j in range(n2):
                int2 = int(num2[j]) * 10 ** (n2 - 1 - j)
                product += int1 * int2
        return str(product)