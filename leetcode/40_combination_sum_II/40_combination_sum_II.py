class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        paths = []
        self.recursive(sorted(candidates), target, 0, [], paths)

        return paths

    def recursive(self, candidates, target, start_index, path, paths):
        if target == 0:
            paths.append(path)

            return None

        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] == candidates[i - 1]:  # skip later duplicate candidates
                continue
            if candidates[i] > target:
                break

            self.recursive(candidates, target - candidates[i], i + 1, path + [candidates[i]], paths)

        return None