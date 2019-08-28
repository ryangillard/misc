class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)):
            if digits[~i] + carry == 10:
                digits[~i] = 0
                carry = 1
            else:
                digits[~i] += carry
                carry = 0

        if carry == 1:
            digits = [1] + digits

        return digits