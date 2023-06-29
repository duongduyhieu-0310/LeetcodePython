#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for i in range(1,n+1):
            a.append(str(i))
        b=[]
        for j in a:
            if int(j)%3==0 and int(j)%5==0:
                b.append("FizzBuzz")
            elif int(j)%5==0:
                b.append("Buzz")
            elif int(j)%3==0:
                b.append("Fizz")
            else:
                b.append(j)
        return b
# @lc code=end

