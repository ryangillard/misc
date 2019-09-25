class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = dict()
        for age in ages:
            count[age] = count.setdefault(age, 0) + 1
            
        friend_requests = 0
        for ageA, countA in count.items():
            for ageB, countB in count.items():
                # Skip all of the nots
                if ageB <= 0.5 * ageA + 7:
                    continue
                if ageB > ageA:
                    continue
                if ageB > 100 and ageA < 100:
                    continue

                # Now actually do something
                friend_requests += countA * countB

                # Fix possible overcounting
                if ageA == ageB:
                    friend_requests -= countA

        return friend_requests