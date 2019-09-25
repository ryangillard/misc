class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        paths = []
        self.recursive(k, n, 1, [], paths)

        return paths

    def recursive(self, k, n, start_index, path, paths):
        if k == 0:
            if n == 0:
                paths.append(path)

            return None
        else:
            for i in range(start_index, 10):
                if i > n:
                    break

                self.recursive(k - 1, n - i, i + 1, path + [i], paths)

        return None