class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for r in nums:
            r.sort(reverse=True)
        n=len(nums)
        m = len(nums[0])
        sum=0
        for j in range(0,m):
            c=0
            for i in range(0,n):
                c=max(c,nums[i][j])
            sum=sum+c
        return sum
        


