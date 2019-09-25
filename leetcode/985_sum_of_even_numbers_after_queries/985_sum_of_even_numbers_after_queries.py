class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        return self.lessIfs(A, queries)

    def moreIfs(self, A, queries):
        current_even_sum = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                current_even_sum += A[i]

        answer = [0] * len(queries)
        for i in range(len(queries)):
            val = queries[i][0]
            idx = queries[i][1]

            if A[idx] % 2 == 0:
                if val % 2 == 0:
                    current_even_sum += val
                else:
                    current_even_sum -= A[idx]
            else:
                if val % 2 == 1:
                    current_even_sum += A[idx] + val

            A[idx] += val

            answer[i] = current_even_sum

        return answer

    def lessIfs(self, A, queries):
        current_even_sum = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                current_even_sum += A[i]

        answer = [0] * len(queries)
        for i in range(len(queries)):
            val = queries[i][0]
            idx = queries[i][1]

            if A[idx] % 2 == 0:
                current_even_sum -= A[idx]

            A[idx] += val

            if A[idx] % 2 == 0:
                current_even_sum += A[idx]

            answer[i] = current_even_sum

        return answer