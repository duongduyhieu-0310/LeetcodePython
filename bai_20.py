#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mappings:
                top_element = stack.pop() if stack else '#'
                
                if mappings[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack
        
# @lc code=end

