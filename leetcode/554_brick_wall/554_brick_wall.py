class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        hash_map = {}

        for row in wall:
            sum = 0
            for brick in row[:-1]:
                sum += brick
                
                hash_map[str(sum)] = hash_map.setdefault(str(sum), 0) + 1

        return len(wall) - max(hash_map.values()) if hash_map else len(wall)