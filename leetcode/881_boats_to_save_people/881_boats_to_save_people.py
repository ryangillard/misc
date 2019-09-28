class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # Greedily add heaviest people and lightest people to boats first
        people.sort()

        boats = 0

        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            boats += 1
            right -= 1

        return boats