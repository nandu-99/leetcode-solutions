class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        best = values[0]
        maxi = 0 
        for j in range(1, len(values)):
            maxi = max(maxi, best+values[j]-j)
            best = max(best, values[j]+j) 
        return maxi 