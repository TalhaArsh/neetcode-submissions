class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            print(c)
            if c in ("(", "{", "["):
                stack.append(c)
                print(stack)
            elif stack and c in (")", "}", "]") and closeToOpen[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack