class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=len(s)-1
        count =0
        for i in range(x,-1,-1):
            if s[i]==" " and count==0:
                continue
            elif s[i]!=" ":
                count+=1
            elif s[i]==" " and count>0:
                break
        return count
