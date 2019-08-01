class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)

        total = [0] * n
        total[0] = cost[0]
        total[1] = cost[1]

        for i in range(2, n - 1):
            total[i] = cost[i] + min(total[i - 1], total[i - 2])

        return min(total[n - 2], total[n - 3] + cost[n - 1])