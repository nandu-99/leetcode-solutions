class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1+cost2<=costBoth:
            return (need1*cost1) + (need2*cost2)
        return min(max(need1, need2)*costBoth, min(need1, need2)*costBoth+abs(need1-need2)*(cost1 if need1>need2 else cost2) )