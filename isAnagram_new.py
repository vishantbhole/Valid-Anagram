class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        l = 0 
        r = len(s)
        sHash = {}
        for a in s:
            sHash[a] = sHash.get(a, 0) + 1
        tHash = {}
        for b in t:
            tHash[b] = tHash.get(b, 0) + 1
        if sHash == tHash:
            return True
        return False


            
