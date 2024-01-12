class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) != 0:
            i = 0
            for x in t:
                if i < len(s):
                    if x == s[i]:
                        i = i + 1
            if i == len(s):
                return True
            else:
                return False
        else:
            return True
