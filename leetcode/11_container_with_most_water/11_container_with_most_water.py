class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            min_height = min(height[left], height[right])
            width = right - left
            area = min_height * width
            max_area = max(max_area, area)
            if height[left] == min_height:
                left += 1
            else:
                right -= 1

        return max_area