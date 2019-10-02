class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        numerator_buffer = ""
        denominator_buffer = ""
        numerator_final = ""
        denominator_final = ""
        writing_numerator = True

        for c in expression:
            if c == "-":
                if denominator_final == "":
                    denominator_final = denominator_buffer
                    denominator_buffer = ""
                else:
                    numerator_final, denominator_final = self.add_frac(numerator_final, denominator_final, numerator_buffer, denominator_buffer)
                writing_numerator = True
                numerator_buffer = c
                denominator_buffer = ""
            elif c == "+":
                if denominator_final == "":
                    denominator_final = denominator_buffer
                    denominator_buffer = ""
                else:
                    numerator_final, denominator_final = self.add_frac(numerator_final, denominator_final, numerator_buffer, denominator_buffer)
                writing_numerator = True
                numerator_buffer = ""
                denominator_buffer = ""
            elif c == "/":
                if numerator_final == "":
                    numerator_final = numerator_buffer
                    numerator_buffer = ""
                writing_numerator = False
            else:
                if writing_numerator:
                    numerator_buffer += c
                else:
                    denominator_buffer += c

        if numerator_buffer == "":
            denominator_final = denominator_buffer
        else:
            numerator_final, denominator_final = self.add_frac(numerator_final, denominator_final, numerator_buffer, denominator_buffer)

        return numerator_final + "/" + denominator_final

    def add_frac(self, numerator_final, denominator_final, numerator_buffer, denominator_buffer):
        A_num = int(numerator_final)
        A_den = int(denominator_final)

        B_num = int(numerator_buffer)
        B_den = int(denominator_buffer)

        num = A_num * B_den + B_num * A_den
        den = A_den * B_den

        temp_gcd = self.gcd(num, den)

        num //= temp_gcd
        den //= temp_gcd

        return str(num), str(den)

    def gcd(self, num, den):
        while den != 0:
            temp = den
            den = num % den
            num = temp

        return abs(num)