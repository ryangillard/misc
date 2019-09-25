class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        n = len(distance)

        # Forward
        forward = 0
        i = start
        while i != destination:
            forward += distance[i]
            i = (i + 1) % n

        # Backward
        backward = 0
        i = (start - 1 + n) % n
        while i + 1 != destination:
            backward += distance[i]
            if backward >= forward:
                break
            i = (i - 1 + n) % n

        return min(forward, backward)