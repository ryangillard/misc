class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        # Make list of points that we can iterate through for distances
        points = [p1, p2, p3, p4]
        
        # Calculate distances between each unique pairing combination, 4 choose 2
        dist = [self.squaredDistance(points[i], points[j]) for i in range(0, 4) for j in range(i + 1, 4)]

        # Sort distances since the 4 sides should be smaller than the 2 diagonals
        dist.sort()
        
        # Make sure each side is the same length x AND that the diagonals are the same length
        # AND that the diagonals are sqrt(2) * x
        if dist[0] == dist[1] == dist[2] == dist[3] > 0 and dist[4] == dist[5] == 2 * dist[0] :
            return True
        else:
            return False
        
    def squaredDistance(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2