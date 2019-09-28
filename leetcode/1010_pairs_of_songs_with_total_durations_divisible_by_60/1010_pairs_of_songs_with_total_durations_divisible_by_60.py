class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        return self.hashmap(time)

    def naive(self, time):
        count = 0
        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1

        return count

    def hashmap(self, time):
        hashmap = dict()
        for i in range(len(time)):
            time[i] = time[i] % 60
            hashmap[time[i]] = hashmap.setdefault(time[i], 0) + 1

        count = 0
        for key, val in hashmap.items():
            if key == 0 or key == 30:
                count += hashmap[key] * (hashmap[key] - 1) // 2  # divide by 2 for double counting
            elif key > 0 and key < 30:
                if 60 - key in hashmap:
                    count += hashmap[key] * hashmap[60 - key]

        return count