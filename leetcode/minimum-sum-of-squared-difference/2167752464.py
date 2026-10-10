class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = []
        for i in range(len(nums1)):
            diff.append(abs(nums1[i]-nums2[i])) 
        if k1+k2==0:
            return sum(a*a for a in diff)
        k = k1+k2 
        if sum(diff)<=k:return 0 
        # heap = []
        # for i in diff:
        #     heapq.heappush(heap, -i)
        # while k:
        #     maxi = -heapq.heappop(heap)
        #     heapq.heappush(heap, -(maxi-1))
        #     k-=1 
        # return sum(a*a for a in heap)
        l, h = 0, max(diff)
        while l < h:
            mid = (l + h) // 2
            ops = sum(max(0, d - mid) for d in diff)

            if ops <= k:
                h = mid
            else:
                l = mid + 1

        rem = k - sum(max(0, d - l) for d in diff)
        diff = [min(d, l) for d in diff]

        for i in range(len(diff)):
            if rem > 0 and diff[i] == l:
                diff[i] -= 1
                rem -= 1

        return sum(d * d for d in diff)