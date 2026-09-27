class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        wind = {}
        thave = Counter(t)
        tneed = defaultdict(int)
        left = right = 0
        res, resLen = [-1, -1], float("inf")
        need, have = len(thave), 0
        while left <= right and right < len(s):
            tneed[s[right]] += 1
            if s[right] in thave and tneed[s[right]] == thave[s[right]]:
                have += 1
            # print(f"tneed = {tneed}, need = {need} and have = {have}")
            while need == have:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                tneed[s[left]] -= 1
                if s[left] in thave and tneed[s[left]] < thave[s[left]]:
                    have -= 1
                left += 1
            right += 1
        return s[res[0]: res[1] + 1] if resLen != float("inf") else ""

