class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        # Get counts
        count_list_of_dicts = []
        for string in A:
            count = {}
            for c in string:
                count[c] = count.setdefault(c, 0) + 1
            count_list_of_dicts.append(count)

        # Find intersection set
        intersection = set(count_list_of_dicts[0].keys())
        for i in range(1, len(count_list_of_dicts)):
            intersection = intersection & set(count_list_of_dicts[i].keys())

        # Find min counts
        ret = []
        for c in intersection:
            min_count = sys.maxint
            for count_dict in count_list_of_dicts:
                min_count = min(min_count, count_dict[c])

            ret.extend([c] * min_count)

        return ret