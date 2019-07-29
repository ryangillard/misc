class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.ptrMethod(nums)

    def sortMethod(self, nums):
        nums_sorted = nums[:]
        nums_sorted.sort()

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i - 1] == nums_sorted[i]:
                return nums_sorted[i]

    def ptrMethod(self, nums):
        # Finds index where they are the same
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        # Find start
        fast = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow