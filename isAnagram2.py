
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash = {}

        if len(s) != len(t):
            return False
        for char in s:
            hash[char] = hash.get(char,0) + 1
        for char in t:
            if char not in hash:
                return False
            count = hash.get(char) - 1
            hash[char] = count
            if count == 0:
                hash.pop(char,None)
        if not hash:
            return True

        return False
            
