class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s, key = str.lower)
        sorted_t = sorted(t, key = str.lower)

        if sorted_s == sorted_t:
            return True
        else:
            return False
        