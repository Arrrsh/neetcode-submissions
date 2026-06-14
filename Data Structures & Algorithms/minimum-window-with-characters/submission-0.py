class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount, window = defaultdict(int), defaultdict(int)
        for c in t:
            tCount[c] += 1
        need, have = len(tCount), 0
        res, resLen = [-1, -1], float("inf")

        left = 0
        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in tCount and window[s[right]] == tCount[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                window[s[left]] -= 1
                if  s[left] in tCount and window[s[left]] < tCount[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left: right + 1] if resLen != float("inf") else ""

