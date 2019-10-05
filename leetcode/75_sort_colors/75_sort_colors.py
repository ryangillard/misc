class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        return self.onePass(nums)

    def twoPass(self, nums):
        count = dict()
        for num in nums:
            count[num] = count.setdefault(num, 0) + 1

        k = 0
        for i in range(3):
            if i in count:
                for j in range(count[i]):
                    nums[k] = i
                    k += 1

        return None

    def onePass(self, nums):
        left, right = 0, len(nums) - 1
        current = 0
        while current <= right:
            if nums[current] < 1:
                nums[current], nums[left] = nums[left], nums[current]
                current += 1
                left += 1
            elif nums[current] > 1:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1