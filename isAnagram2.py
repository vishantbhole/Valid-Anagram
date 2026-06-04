
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash = {}

        if len(s) != len(t):
            return False
        for char in s:
            hash[char] = hash.get(char,0) + 1
