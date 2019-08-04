class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rec1 = (C - A) * (D - B)
        rec2 = (G - E) * (H - F)

        # If no intersection
        if E >= C or A >= G or F >= D or B >= H:
            return rec1 + rec2

        # Sort the 4 X's and 4 Y's
        sorted_x = sorted([A, E, C, G])
        sorted_y = sorted([F, B, H, D])

        return rec1 + rec2 - (sorted_x[2] - sorted_x[1]) * (sorted_y[2] - sorted_y[1])