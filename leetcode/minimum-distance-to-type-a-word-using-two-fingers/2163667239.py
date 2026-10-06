class Solution:
    def minimumDistance(self, word: str) -> int:
        n =len(word)
        def pos(c):
            x = ord(c)-ord('A')
            return x//6, x%6 
        
        def dist(a, b):
            if a==26 or b==26:return 0 
            x1, y1 = pos(chr(a+ord('A')))
            x2, y2 = pos(chr(b+ord('A')))
            return abs(x1-x2)+abs(y1-y2)
        
        d ={}

        def recur(i, l, r):
            if i==n:return 0 
            if (i, l, r) in d: return d[(i, l, r)]
            curr = ord(word[i])-ord('A')
            ml = dist(l, curr)+recur(i+1, curr, r)
            mr = dist(r, curr)+recur(i+1, l, curr)
            d[(i, l, r)] = min(ml, mr)
            return d[(i, l, r)]
        return recur(0, 26, 26)
