class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        res = 0
        win = set()
        while left <= right and right < len(s):
            while s[right] in win:
                win.remove(s[left])
                left += 1
            win.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        return res