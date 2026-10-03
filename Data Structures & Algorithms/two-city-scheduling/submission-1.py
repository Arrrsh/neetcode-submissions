class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res, n = 0, len(costs) // 2
        costs.sort(key=lambda x : x[1] - x[0])
        for i in range(n):
            res += costs[i][1] + costs[i + n][0]
        return res
        
        