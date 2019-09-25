class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        paths = []
        self.recursive(candidates, target, 0, [], paths)

        return paths

    def recursive(self, candidates, target, start_index, path, paths):
        if target == 0:
            paths.append(path)

            return None

        for i in range(start_index, len(candidates)):
            if candidates[i] <= target:
                self.recursive(candidates, target - candidates[i], i, path + [candidates[i]], paths)

        return None