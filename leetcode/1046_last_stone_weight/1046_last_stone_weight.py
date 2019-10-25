class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while True:
            if not stones:
                return 0
            elif len(stones) == 1:
                return stones[0]

            stones.sort()
            if stones[-2] == stones[-1]:
                stones = stones[:-2]
            else:
                stones = stones[:-2] + [stones[-1] - stones[-2]]