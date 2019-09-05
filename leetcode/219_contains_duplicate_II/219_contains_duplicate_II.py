class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        return self.hashmapMethod(nums, k)

    def hashmapMethod(self, nums, k):
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.setdefault(num, 0) + 1

        index_map = {}
        diff_map = {}
        for i, num in enumerate(nums):
            if hashmap[num] > 1:
                if num in index_map:
                    if not diff_map.get(num) or not diff_map[num]:
                        diff_map[num] = i - index_map[num] <= k

                index_map[num] = i

        return any(diff_map.values())