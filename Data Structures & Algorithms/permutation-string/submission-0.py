class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            w = s2[left: right + 1]
            s2_cnt = Counter(w)
            if s1_counter == s2_cnt:
                return True
            left += 1
            right += 1
        return False