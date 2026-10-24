class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
        def convert(s):
            m, d = map(int, s.split("-"))
            return sum(days[:m-1])+d 
        
        s = max(convert(arriveAlice), convert(arriveBob))
        e = min(convert(leaveAlice), convert(leaveBob))
        return max(0, e-s+1)

