class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        found_double = False
        read = 1
        write = 1
        while read < len(nums):
            if nums[read] == nums[read - 1]:
                if not found_double:
                    nums[write] = nums[read]
                    found_double = True
                    write += 1
            else:
                nums[write] = nums[read]
                found_double = False
                write += 1
            read += 1

        return write