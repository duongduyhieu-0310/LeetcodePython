class Solution:
    def minLength(self, s: str) -> int:
        AB1 = False
        CD2= False
        while True :
            if "AB" in s :
                s = s.replace("AB","")
                AB1 = True
            else :
                AB1 = False
                
            if "CD" in s :
                s = s.replace("CD","")
                CD2 = True
            else :
                CD2 = False
            
            if not AB1 and not CD2 :
                return len(s)