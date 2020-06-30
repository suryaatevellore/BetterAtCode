class Solution:
    def check_subsequence(self, s, t):
        if not s:
            return True
        if not t and s:
            return False
        if len(s) == 1 and len(t)==1:
            return True if s[0] == t[0] else False
        if s[0] == t[0]:
            return self.check_subsequence(s[1:], t[1:]) 
        if s[0]!=t[0]:
            return self.check_subsequence(s, t[1:])

    def isSubsequence(self, s: str, t: str) -> bool:
        return self.check_subsequence(s, t)
