class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        right = [n] * n
        left = [-1] * n
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                right[stack[-1]] = i
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        res = max(h * (right[i] - left[i] - 1) for i, h in enumerate(heights))
        return res
