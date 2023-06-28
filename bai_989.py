#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
         # chuyển mảng về dạng số nguyên 

        numsk = int(''.join(map(str,num)))
    # tổng các số 
        sumk=numsk+k
    #chuyển về dạng mảng 
        nums=[int(x) for x in str(sumk)]
        return nums
          
     
# @lc code=end

