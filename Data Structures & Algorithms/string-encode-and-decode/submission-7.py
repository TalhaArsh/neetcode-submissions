class Solution:

    def encode(self, strs: List[str]) -> str:
        res =""
        for s in strs:
            res += str(len(s)) + ":" + s
        
        return res
    # 100::xneudhshsdh...
    def decode(self, s: str) -> List[str]:
        res,i =[] ,0
        
        while i < len(s):
            rightptr = i
            while s[rightptr] != ":":
                rightptr += 1
            strlength = int (s[i:rightptr])
            res .append(s[rightptr + 1 : rightptr + 1 + strlength])
            i = rightptr + 1 + strlength
            
        return res
        


