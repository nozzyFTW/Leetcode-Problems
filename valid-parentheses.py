class Solution:
    def isValid(self, s: str) -> bool:
        left_parentheses = []
        for char in s:
            if char in ["(", "{", "["]:
                left_parentheses.append(char)
            
            elif char == ")" and len(left_parentheses) != 0 and left_parentheses[-1] == "(":
                left_parentheses.pop()
            elif char == "}" and len(left_parentheses) != 0 and left_parentheses[-1] == "{":
                left_parentheses.pop()
            elif char == "]" and len(left_parentheses) != 0 and left_parentheses[-1] == "[":
                left_parentheses.pop()
            else:
                return False
        return left_parentheses == []