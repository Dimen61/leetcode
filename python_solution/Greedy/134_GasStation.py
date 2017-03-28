# Two key points:
# (1) Assume B is the first station which A could not reach, so any station
#     between A and B could not reach B.
# (2) If sum(gas) >= cost, there must be a solution. Use method of induction
#     to proof it.
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or sum(cost) > sum(gas):
            return -1
        
        start = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1
        return start