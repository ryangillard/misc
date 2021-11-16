class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows, cols = len(image), len(image[0])
        old_color = image[sr][sc]

        if newColor == old_color:  # no change
            return image

        def dfs(row, col):
            if image[row][col] == old_color:
                image[row][col] = newColor
                if row - 1 >= 0:
                    dfs(row - 1, col)
                if row + 1 < rows:
                    dfs(row + 1, col)
                if col - 1 >= 0:
                    dfs(row, col - 1)
                if col + 1 < cols:
                    dfs(row, col + 1)

        dfs(sr, sc)
        return image