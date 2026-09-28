class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []
        a = 0
        b = 0

        for t in tokens:
            if t in ('+','-','*','/'):
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    res = a + b
                elif t == '-':
                    res = b - a
                elif t == '*':
                    res = a * b
                else:
                    res = int(float(b)/a)
                print(res)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]
               
        