class Solution(object):
    def __init__(self):
        self.count = 0
        self.kth_perm = ""

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.fast_iterative(n, k, [str(i) for i in range(1, n + 1)])

        return self.kth_perm

    def slow_recursive(self, k, nums, path):
        if len(nums) == 0:
            self.count += 1
            if self.count == k:
                self.kth_perm = "".join(path)

            return None

        for i in range(len(nums)):
            if self.kth_perm == "":
                self.slow_recursive(k, nums[:i] + nums[i + 1:], path + [nums[i]])
            else:
                return None

        return None

    def fast_iterative(self, n, k, nums):
        factorial = [1] * (n + 1)
        for i in range(1, len(factorial)):
            factorial[i] = factorial[i - 1] * i

        kth_seq = []
        for i in range(1, n + 1):
            idx = (k - 1) // factorial[n - i]
            kth_seq.append(nums[idx])
            del nums[idx]
            k -= idx * factorial[n - i]

        self.kth_perm = "".join(kth_seq)

        return None