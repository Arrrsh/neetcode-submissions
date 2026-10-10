class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                substring = ""
                while stack and stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(substring * int(k))
        return "".join(stack)
