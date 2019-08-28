class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        i = len(A) - 1
        carry = 0
        K_count = 0
        while K != 0 and i >= 0:
            digit = K % 10
            K /= 10
            K_count += 1
            if A[i] + carry + digit > 9:
                A[i] = (A[i] + carry + digit) % 10
                carry = 1
            else:
                A[i] += carry + digit
                carry = 0

            i -= 1

        while carry == 1 and i >= 0:
            if A[i] + carry > 9:
                A[i] = 0
                carry = 1
            else:
                A[i] += carry
                carry = 0

            i -= 1

        while K != 0:
            digit = K % 10
            K /= 10
            K_count += 1
            
            if K_count == len(A):
                if A[0] + digit > 9:
                    A[0] = 0
                    carry = 1
                else:
                    A[0] += digit
            else:
                if digit + carry > 9:
                    A = [0] + A
                    carry = 1
                else:
                    A = [digit + carry] + A
                    carry = 0

        if carry == 1:
            A = [1] + A
            carry = 0

        return A