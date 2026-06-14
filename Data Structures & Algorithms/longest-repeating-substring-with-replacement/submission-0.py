class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = Counter()
        left = 0
        max_freq = 0
        for right, char in enumerate(s):
            char_count[char] += 1

            max_freq = max(max_freq, char_count[char])

            if right - left + 1 - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
        #  Since we only shrink when invalid, the window maintains max valid size
        return len(s) - left