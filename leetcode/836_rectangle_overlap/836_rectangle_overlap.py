class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or  # rec1 is too far left from rec2
                    rec1[0] >= rec2[2] or  # rec1 is too far right from rec2
                    rec1[3] <= rec2[1] or  # rec1 is too far down from rec2
                    rec1[1] >= rec2[3])  # rec1 is too far up from rec2