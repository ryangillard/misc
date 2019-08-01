class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        seq = "11"
        
        if n == 2:
            return seq

        for _ in range(2, n):
            string_builder = []
            prev_val = seq[0]
            count = 1
            for i in range(1, len(seq)):
                if seq[i] == prev_val:
                    count += 1
                else:
                    string_builder.append(str(count) + str(prev_val))
                    prev_val = seq[i]
                    count = 1
            string_builder.append(str(count) + str(prev_val))
            seq = "".join(string_builder)

        return seq