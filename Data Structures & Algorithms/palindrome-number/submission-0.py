class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        if x > 0 and x % 10 == 0:
            return False
        div = 1
        while x >= div * 10:
            div *= 10
        while x:
            right_digit  = x % 10
            left_digit = x // div
            if left_digit != right_digit: return False

            x = (x % div) // 10
            div = div // 100
        return True