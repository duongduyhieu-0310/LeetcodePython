#
# @lc app=leetcode id=2165 lang=python3
#
# [2165] Smallest Value of the Rearranged Number
#

# @lc code=start
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            num_string = ''.join(sorted(str(num).replace("0","")))
            missing_zero = '0' * (len(str(num)) - len(num_string))
            return int(num_string[0] + missing_zero + num_string[1:])
        elif num < 0:
            num_string = ''.join(sorted(str(num)[1:].replace("0", ""), reverse=True))
            missing_zero = '0' * (len(str(num)) - len(num_string) - 1)
            return int("-" + num_string[0] + num_string[1:] + missing_zero)
        else:
            return 0



    
# @lc code=end

