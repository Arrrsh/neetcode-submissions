class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = int(tokens[0])

        stack = []
        op = lambda a, b, c: a + b if c == "+" else a - b if c == "-" else a * b if c == "*" else a / b if c == "/" else None
        for c in tokens:
            if c in "+-*/":
                a = stack.pop()
                b = stack.pop()
                C = op(int(b), int(a), c)
                stack.append(C)
            else:
                stack.append(c)
        print(stack)
        return int(stack[0]) if stack else res