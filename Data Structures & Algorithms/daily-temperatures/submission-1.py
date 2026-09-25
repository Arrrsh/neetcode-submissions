class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n = len(temperatures)
        # res = [0] * n
        # stack = []
        # for i, t in enumerate(temperatures):
        #     while stack and temperatures[stack[-1]] < t:
        #         last = stack.pop()
        #         res[last] = i - last
        #     stack.append(i)
        # return res
        stack = []
        res = [0] * len(temperatures)
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res