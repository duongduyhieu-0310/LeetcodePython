class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        a=[]
        for i in arr:
            x=arr.count(i)
            y=i 
            a.append([x,y])
        a.sort()
        l=len(a)
        z= a[l-1][1]
        return z