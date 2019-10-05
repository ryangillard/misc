class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.dictionary(numbers, target)

    def twoPointer(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            summ = numbers[left] + numbers[right]
            if summ == target:
                return [left + 1, right + 1]
            elif summ < target:
                left += 1
            else:
                right -= 1

        return None

    def dictionary(self, numbers, target):
        diff_dict = dict()
        for i in range(len(numbers)):
            if target - numbers[i] in diff_dict:
                return [diff_dict[target - numbers[i]] + 1, i + 1]
            diff_dict[numbers[i]] = i