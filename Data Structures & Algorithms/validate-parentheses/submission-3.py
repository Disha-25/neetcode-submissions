class Solution:
    def isValid(self, s: str) -> bool:
        # (){
        brackets = dict({
            ")":"(",
            "]":"[",
            "}":"{"
        })
        stack = []
        for char in s:
            if char in brackets.values():
                stack.append(char)
            else:
                if not stack: return False
                if stack[-1] != brackets[char]:
                    return False
                stack.pop()
        return not stack