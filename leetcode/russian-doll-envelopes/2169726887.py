class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # envelopes.sort(key = lambda x: (x[0], -x[1]))
        # height = [envelope[1] for envelope in envelopes]
        # d = {}
        # def recur(i, pre):
        #     if (i, pre) in d:return d[(i, pre)]
        #     if i==len(height):return 0 
        #     t = 0 
        #     if pre==-1 or height[i]>height[pre]:
        #         t = recur(i+1, i)+1 
        #     nt = recur(i+1, pre)
        #     d[(i, pre)] = max(t, nt)
        #     return d[(i, pre)]
        # return recur(0, -1)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []

        for _, h in envelopes:
            i = bisect_left(lis, h)

            if i == len(lis):
                lis.append(h)
            else:
                lis[i] = h

        return len(lis)