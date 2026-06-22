class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char not in bracket_map:
                stack.append(char)
            
            else:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                
                if stack[-1] == bracket_map[char]:
                    stack.pop()
        
        return len(stack) == 0