from typing import List

class Solution:
    @classmethod
    def reverseString(cls, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        n = len(s)
        i = 0
        j = n-1
        while(j>i):
            s[i],s[j] = s[j], s[i]
            i+=1
            j-=1

        print(s)
