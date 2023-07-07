#
# @lc app=leetcode id=2126 lang=python3
#
# [2126] Destroying Asteroids
#

# @lc code=start
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for i in asteroids :
            if mass>=i:
                mass=mass+i
            else:
                return False
        if mass>0:
            return True
# @lc code=end

