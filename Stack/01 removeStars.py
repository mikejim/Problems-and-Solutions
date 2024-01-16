class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if c == "*":
                stack.pop()
                stack.pop()
        i = 0
        x = ""
        tam = len(stack)
        while i < tam:
            x = stack.pop() + x
            i = i + 1
        return x 
    