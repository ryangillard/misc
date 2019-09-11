class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        let_logs = []
        dig_logs = []
        for log in logs:
            if log.split()[1].isdigit():  # first word after identifier
                dig_logs.append(log)
            else:
                let_logs.append(log)

        let_logs.sort(key=lambda s: (s[s.index(" ") + 1:], s[:s.index(" ")]))  #lexicographic sort

        return let_logs + dig_logs