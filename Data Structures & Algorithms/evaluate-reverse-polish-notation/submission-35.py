class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []
        operators = set(["+", "-", "*", "/"])
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(self.operation(first, second, t))

        return stack[-1]

    def operation(self, first, second, operator):
        if operator == "+":
            return first + second
        elif operator == "*":
            return first * second
        elif operator == "/":
            return int(first / second)
        elif operator == "-":
            return first - second

        