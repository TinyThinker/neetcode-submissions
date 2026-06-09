class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"*", "-", "/", "+"}:
                stack.append(int(token))
            else:
                print(f"Token = {token}, Stack = {stack}")
                b = stack.pop()
                a = stack.pop()

                result = None
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:
                    result = int(a / b)
                
                stack.append(result)

        return stack[-1]
        