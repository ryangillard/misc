class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        intersection = set(list1) & set(list2)

        dict1 = {val: i + 1 for i, val in enumerate(list1) if val in intersection}
        dict2 = {val: i + 1 for i, val in enumerate(list2) if val in intersection}

        min_val = []
        min_sum = sys.maxint

        for val in intersection:
            if val in dict1 and val in dict2:
                if dict1[val] + dict2[val] < min_sum:
                    min_sum = dict1[val] + dict2[val]
                    min_val = [val]
                elif dict1[val] + dict2[val] == min_sum:
                    min_val.append(val)

        return min_val