class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        idx = sorted(range(len(position)), key= lambda i: position[i])
        ans = pre = 0
        for i in idx[::-1]: # Closest to farthest
            # Calculate time for current car to reach target
            t = (target - position[i]) / speed[i]
            if t > pre:
                ans += 1
                pre = t
        return ans