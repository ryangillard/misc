import random

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.points_per_rect_cum_sum = self._find_points_cum_sum()
        self.max_points = self.points_per_rect_cum_sum[-1]

    def _find_points_cum_sum(self):
        def _find_dims(i):
            h = self.rects[i][3] - self.rects[i][1]
            w = self.rects[i][2] - self.rects[i][0]

            return h, w

        cum_sum = [0] * len(self.rects)

        h, w = _find_dims(0)
        cum_sum[0] = (h + 1) * (w + 1)

        for i in range(1, len(self.rects)):
            h, w = _find_dims(i)
            cum_sum[i] = (h + 1) * (w + 1) + cum_sum[i - 1]

        return cum_sum

    def pick(self):
        """
        :rtype: List[int]
        """
        # Choose a point across all rectangles
        point_idx = random.randint(0, self.max_points - 1)

        # Find which rectangle point belongs
        point_rect_idx = point_idx
        for i in range(len(self.points_per_rect_cum_sum)):
            if point_idx < self.points_per_rect_cum_sum[i]:
                if i > 0:
                    point_rect_idx = point_idx - self.points_per_rect_cum_sum[i - 1]
                rect_idx = i
                break

        # Find point coordinates in rectangle
        rect = self.rects[rect_idx]

        w = rect[2] - rect[0]

        return [rect[0] + point_rect_idx % (w + 1), rect[1] + point_rect_idx // (w + 1)]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()