class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        my_bills = [0] * 3
        bill_indices = {5: 0, 10: 1, 20: 2}
        for i in range(len(bills)):
            if bills[i] == 10:
                if my_bills[bill_indices[5]] < 1:
                    return False
                my_bills[bill_indices[5]] -= 1
            elif bills[i] == 20:
                if my_bills[bill_indices[10]] < 1:
                    if my_bills[bill_indices[5]] < 3:
                        return False
                    my_bills[bill_indices[5]] -= 3
                else:
                    if my_bills[bill_indices[5]] < 1:
                        return False
                    my_bills[bill_indices[10]] -= 1
                    my_bills[bill_indices[5]] -= 1

            my_bills[bill_indices[bills[i]]] += 1

        return True