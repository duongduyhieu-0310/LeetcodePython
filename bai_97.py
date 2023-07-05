#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3): return False
        
        memMap = {}
        
        def interleave(i1, i2, i3):
            if (i1,i2) in memMap:
                return memMap[(i1, i2)]
            if i3 == len(s3):
                return True
            
            found = False
            if i1 < len(s1) and s3[i3] == s1[i1]:
                found = found or interleave(i1+1, i2, i3+1)
            if i2 < len(s2) and s3[i3] == s2[i2]:
                found = found or interleave(i1, i2+1, i3+1)
                
            memMap[(i1, i2)] = found
            return found
        
        return interleave(0, 0, 0)
# @lc code=end

