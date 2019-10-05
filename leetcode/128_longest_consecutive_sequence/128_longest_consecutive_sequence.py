class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert to set to get rid of duplicates
        nums_set = set(nums)

        # Iterate through numbers in set
        longest = 0
        for num in nums_set:
            # If previous number is not in set, then we no this is the beginning of a sequence
            if num - 1 not in nums_set:
                next_num = num + 1
                # Check to see if we can go further in the sequence
                while next_num in nums_set:
                    next_num += 1

                # Update the longest in case we actually got anywhere
                longest = max(longest, next_num - num)

        return longest