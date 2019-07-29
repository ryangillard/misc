class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.binary_search(nums, target)

    def linear_search(self, nums, target):
        ret = [-1, -1]
        for idx, num in enumerate(nums):
            if num == target:
                if ret[0] == -1:
                    ret[0] = idx
                    ret[1] = idx
                else:
                    ret[1] = idx
            elif num > target:
                break

        return ret

    def builtin_search(self, nums, target):  
        count = nums.count(target)

        if count == 0:
            return [-1, -1]
        else:
            start = nums.index(target)
            return [start, start + count - 1]
        
    def binary_search(self, nums, target):
        ret = [-1, -1]

        # Fin start index
        left_idx = 0
        right_idx = len(nums)

        while left_idx < right_idx:
            half = (left_idx + right_idx) // 2
            pivot = nums[half]

            if pivot >= target:
                right_idx = half
            else:
                left_idx = half + 1

        if left_idx == len(nums) or nums[left_idx] != target:
            return ret

        ret[0] = left_idx

        # Find end index
        left_idx = 0
        right_idx = len(nums)

        while left_idx < right_idx:
            half = (left_idx + right_idx) // 2
            pivot = nums[half]

            if pivot > target:
                right_idx = half
            else:
                left_idx = half + 1
                
        ret[1] = left_idx - 1
        
        return ret