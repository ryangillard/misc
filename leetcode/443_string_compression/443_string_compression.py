class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1

        idx_start = 0
        idx_end = 0
        for i in range(len(chars)):
            if i + 1 == len(chars) or chars[i + 1] != chars[i]:
                # New character or end of string
                chars[idx_end] = chars[idx_start]
                idx_end += 1
                
                if i > idx_start:
                    # If there were duplicates of character
                    str_count = str(i - idx_start + 1)

                    # Add digits
                    for j in range(len(str_count)):
                        chars[idx_end] = str_count[j]
                        idx_end += 1

                idx_start = i + 1

        return idx_end