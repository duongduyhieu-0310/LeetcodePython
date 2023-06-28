#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x  =  set(ransomNote)
        x  =  list(x)
        for i in x :
            if magazine.count(i)  <  ransomNote.count(i):
                return False
        return True
		
# @lc code=end

