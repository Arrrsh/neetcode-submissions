import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [(-v, i) for i, v in enumerate(nums[: k -1])]
        heapq.heapify(q)

        res = []

        for i in range(k - 1, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res