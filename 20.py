class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"(":")","{":"}","[":"]"}
        for parenthese in s :
            if parenthese in lookup:
                stack.append(parenthese)
                #{[]}
            
            elif len(stack)==0 or lookup[stack.pop()]!=parenthese:
                return False
        
            