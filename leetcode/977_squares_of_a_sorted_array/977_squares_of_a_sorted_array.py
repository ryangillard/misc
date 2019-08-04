class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return self.twoPointers(A)

    def naiveSort(self, A):
        return sorted([x ** 2 for x in A])
    
    def twoPointers(self, A):
        length = len(A)

        # Find the index where positive numbers start
        pos_start_idx = 0
        while pos_start_idx < length and A[pos_start_idx] < 0:
            pos_start_idx += 1
        neg_end_idx = pos_start_idx - 1

        # Square numbers
        A = [x ** 2 for x in A]

        ans = []
        # Move both pointers until one or both hit the end of the list
        while 0 <= neg_end_idx and pos_start_idx < length:
            if A[pos_start_idx] < A[neg_end_idx]:
                ans.append(A[pos_start_idx])
                pos_start_idx += 1
            else:
                ans.append(A[neg_end_idx])
                neg_end_idx -= 1

        # Finish adding any remaining squared negatives
        while neg_end_idx >= 0:
            ans.append(A[neg_end_idx])
            neg_end_idx -= 1

        # Finish adding any remaining squared positives
        while pos_start_idx < length:
            ans.append(A[pos_start_idx])
            pos_start_idx += 1

        return ans