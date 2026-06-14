class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            n = len(s)
            ans += f"{n:04d}" + s
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        while len(s) > 0:
            l = int(s[:4])
            ans.append(s[4: 4 + l])
            s = s[4 + l :]
        return ans