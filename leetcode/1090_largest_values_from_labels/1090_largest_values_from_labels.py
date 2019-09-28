class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        sorted_value_label_tuples = sorted(zip(values, labels), reverse=True)
        
        label_counts = dict()
        total = 0
        for value, label in sorted_value_label_tuples:
            if label not in label_counts:
                label_counts[label] = 0

            if label_counts[label] < use_limit:
                label_counts[label] += 1
                total += value
                num_wanted -= 1
                if num_wanted == 0:
                    break

        return total