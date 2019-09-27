class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.posNegWithoutTemp(nums)

    def naive(self, nums):
        max_product = -sys.maxint

        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                if product > max_product:
                    max_product = product

        return max_product

    def prefixSuffix(self, nums):
        prefix = nums
        suffix = nums[::-1]
        for i in range(1, len(nums)):
            prefix[i] *= 1 if prefix[i - 1] == 0 else prefix[i - 1]
            suffix[i] *= 1 if suffix[i - 1] == 0 else suffix[i - 1]

        return max(prefix + suffix)
    
    def posNegWithTemp(self, nums):
        if len(nums) == 1:
            return nums[0]

        pos_product = 0
        neg_product = 0
        max_product = 0

        for i in range(len(nums)):
            temp_pos_product = max(nums[i], nums[i] * pos_product, nums[i] * neg_product)
            neg_product = min(nums[i], nums[i] * pos_product, nums[i] * neg_product)
            pos_product = temp_pos_product
            max_product = max(pos_product, neg_product, max_product)

        return max_product

    def posNegWithoutTemp(self, nums):
        if len(nums) == 1:
            return nums[0]

        pos_product = 0
        neg_product = 0
        max_product = 0

        for i in range(len(nums)):
            pos_product, neg_product = max(nums[i], nums[i] * pos_product, nums[i] * neg_product), min(nums[i], nums[i] * pos_product, nums[i] * neg_product)
            max_product = max(pos_product, neg_product, max_product)

        return max_product