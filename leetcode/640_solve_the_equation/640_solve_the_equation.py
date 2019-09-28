class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        # Condense equation
        x = 0
        constant = 0

        buf = ""
        lhs = True
        for i in range(len(equation)):
            if equation[i] == "=":
                # Switch sides
                if buf != "":
                    constant -= int(buf)
                buf = ""
                lhs = False
            elif equation[i] == "+":
                # Push constant
                if buf != "":
                    if lhs:
                        constant -= int(buf)
                    else:
                        constant += int(buf)
                    buf = ""
            elif equation[i] == "-":
                # Push constant
                if buf != "":
                    if lhs:
                        constant -= int(buf)
                    else:
                        constant += int(buf)
                buf = "-"
            elif equation[i] == "x":
                # Push x
                if buf == "":
                    buf = "1"
                elif buf == "-":
                    buf = "-1"

                if lhs:
                    x += int(buf)
                else:
                    x -= int(buf)
                buf = ""
            else:
                buf += equation[i]

        # In case last element was a constant
        if buf != "":
            constant += int(buf)

        # Check equation
        if constant == 0:
            if x == 0:
                return "Infinite solutions"
            else:
                return "x=0"
        else:
            if x == 0:
                return "No solution"

        return "x=" + str(constant / x)