class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if (sum(gas) - sum(cost)) < 0:
            return -1

        return self.optimized(gas, cost)

    def bruteForce(self, gas, cost):
        n_stations = len(gas)

        for i in range(0, n_stations):
            # Start at station i
            tank = gas[i]
            for j in range(1, n_stations):
                cost_index = (i + j - 1) % n_stations
                gas_index = (i + j) % n_stations
                tank -= cost[cost_index]

                if tank <= 0:
                    break

                tank += gas[gas_index]

            # Check if we made it back around
            if tank >= cost[(i + n_stations - 1) % n_stations]:
                return i

        return -1

    def optimized(self, gas, cost):
        n_stations = len(gas)

        tank = 0
        start_idx  = 0
        current_idx  = 0
        while True:
            tank += gas[current_idx]
            # If car can't make it to next station, reset
            if tank - cost[current_idx] < 0:
                tank = 0
                start_idx = (current_idx + 1) % n_stations
                current_idx = start_idx
                continue
            tank -= cost[current_idx]
            current_idx = (current_idx + 1) % n_stations

            # Check if we made it back around
            if start_idx == current_idx:
                return start_idx