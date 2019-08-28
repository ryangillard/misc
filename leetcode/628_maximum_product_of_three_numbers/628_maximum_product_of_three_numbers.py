class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 3
        if len(nums) == count:
            return nums[0] * nums[1] * nums[2]
        
        big_num = 9999999
        negatives = [big_num] * 3
        positives = [-big_num] * 3

        for num in nums:
            if num < 0:
                for i in range(count):
                    if num < negatives[i]:
                        negatives[i] = num
                        negatives = sorted(negatives)[::-1]
                        break
            else:
                for i in range(count):
                    if num > positives[i]:
                        positives[i] = num
                        positives = sorted(positives)
                        break
                        
        negatives = negatives[::-1]
        positives = positives[::-1]

        num_neg = 0
        num_pos = 0

        for i in range(count):
            if negatives[i] != big_num:
                num_neg += 1
            else:
                break
                
        for i in range(count):
            if positives[i] != -big_num:
                num_pos += 1
            else:
                break
        
        if num_pos == count:
            if num_neg <= 1:
                return positives[0] * positives[1] * positives[2]
            return max(negatives[0] * negatives[1] * positives[0], positives[0] * positives[1] * positives[2])
        elif num_pos == 2:
            if num_neg == 2:
                return max(negatives[0] * negatives[1] * positives[0], negatives[0] * positives[0] * positives[1])
            return max(negatives[0] * negatives[1] * negatives[2], negatives[0] * positives[0] * positives[1])
        elif num_pos == 1:
            return max(negatives[0] * negatives[1] * negatives[2], negatives[0] * negatives[1] * positives[0])
        else:
            return negatives[0] * negatives[1] * negatives[2]