#
# @lc app=leetcode id=2164 lang=python3
#
# [2164] Sort Even and Odd Indices Independently
#

# @lc code=start
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        l1 = []
        l2 = []
        for i in range(len(nums)):
            if i%2==0:
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        l1.sort()
        l2.sort(reverse=True)

        l3 = []
        a = 0 
        for i in range(len(l1)):
            l3.insert(a,l1[i])
            a+=2
        b = 1 
        for g in range(len(l2)):
            l3.insert(b,l2[g])
            b+=2
        return l3 
# @lc code=end

