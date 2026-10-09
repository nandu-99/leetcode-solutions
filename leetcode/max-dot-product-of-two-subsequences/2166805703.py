class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        d = {}
        def recur(i, j):
            if (i, j) in d:return d[(i, j)]
            if i>=len(nums1) or j>=len(nums2): return float('-inf') 
            pro = nums1[i]*nums2[j]
            t = pro+max(0, recur(i+1, j+1))
            nt = recur(i+1, j)
            ntt = recur(i, j+1)
            d[(i, j)] = max(t, nt, ntt)
            return d[(i, j)]
        return recur(0, 0)