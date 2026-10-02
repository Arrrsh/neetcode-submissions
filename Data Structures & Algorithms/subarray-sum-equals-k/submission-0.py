class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0 : 1}
        curr = 0
        res = 0
        for n in nums:
            curr += n
            diff = curr - k
            if diff in prefixSum:
                res += prefixSum[diff]
            prefixSum[curr] = 1 + prefixSum.get(curr, 0)
        return res
