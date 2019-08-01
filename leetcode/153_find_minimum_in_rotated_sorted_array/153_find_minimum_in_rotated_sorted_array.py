class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.binary_search(nums)


    def linear_min(self, nums):
        minimum = sys.maxsize

        for num in nums:
            if num < minimum:
                minimum = num

        return minimum


    def linear_inflect(self, nums):
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:

                return nums[i + 1]


    def builtin(self, nums):
        return min(nums)


    def sort(self, nums):
        return sorted(nums)[0]


    def binary_search(self, nums):
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        if nums[0] < nums[-1]:
            return nums[0]

        while left <= right:
            mid = left + (right - left) // 2

            # Check both sides of mid
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # Check which subarray
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1