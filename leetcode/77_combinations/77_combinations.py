class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        paths = []
        self.recursive(n, k, 1, [], paths)

        return paths

    def recursive(self, n, k, start_index, path, paths):
        if k == 0:
            paths.append(path)

            return None

        for i in range(start_index, n + 1):
            self.recursive(n, k - 1, i + 1, path + [i], paths)

        return None