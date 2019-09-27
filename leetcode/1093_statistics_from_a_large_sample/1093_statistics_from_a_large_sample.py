class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        # Find minimum
        for i in range(len(count)):
            if count[i] > 0:
                minimum = i
                break

        # Find maximum
        for i in range(len(count) - 1, minimum, -1):
            if count[i] > 0:
                maximum = i
                break

        # Find mean and mode
        mean_count = 0
        mean_sum = 0
        mode_count = 0
        for i in range(minimum, maximum + 1):
            if count[i] > 0:
                mean_count += count[i]
                mean_sum += count[i] * i

                if count[i] > mode_count:
                    mode_count = count[i]
                    mode = i
        mean = float(mean_sum) / mean_count

        # Find median
        half_count = mean_count // 2
        median_count = 0
        for i in range(minimum, maximum + 1):
            if count[i] > 0:
                median_count += count[i]
                if median_count > half_count:
                    median = float(i)
                    break
                elif median_count == half_count:
                    if mean_count % 2 == 0:
                        median = (2.0 * i + 1.0) / 2.0
                    else:
                        median = float(i)
                    break

        return [float(minimum), float(maximum), mean, median, float(mode)]