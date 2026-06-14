class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        w = set()
        while right < len(s):
            while s[right] in w:
                w.remove(s[left])
                left += 1
            w.add(s[right])
            res = max(res, len(w))
            right += 1
        return res