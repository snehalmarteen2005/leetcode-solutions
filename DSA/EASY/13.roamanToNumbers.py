class Solution:
    def romanToInt(self, s: str) -> int:
        dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        x=0
        total=0
        while x < len(s):
            if x+1 < len(s) and dict[s[x]]<dict[s[x+1]]:
                total+=dict[s[x+1]]-dict[s[x]]
                x+=2
            else:
                total+=dict[s[x]]
                x+=1
        return total
        
