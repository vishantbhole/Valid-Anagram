class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tlen =len(t)
        slen = len(s)
        char_map_s = {}
        char_map_t = {}

        if (tlen != slen):
            return False
        for i in range(slen):
            char_map_s[s[i]] = char_map_s.get(s[i], 0) + 1
            char_map_t[t[i]] = char_map_t.get(t[i], 0) + 1
        for c in char_map_s:
            if char_map_s[c] != char_map_t.get(c,0):
                return False
        return True
