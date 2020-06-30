# from Rabin_carp import rabin_carp
from rabin_carp_git import rabin_karp

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        i = 0
        j = 1
        found = []
        while(j<=len(S)):
            print(f"i={i}, j={j}")
            print(f"Testing for {S[i:j]}")
            rc_result = rabin_karp(S[i:j], S[i+1:])
            print(f"Was {S[i:j]} found ? {rc_result}")
            # if len(rc_result) != 1:
            if rc_result !=-1:
                # duplicate found
                found.append((i, j))
                j+=1
            else:
                i+=1
                j+=1

        print(found)
        # if len(found) == 1:
        #     return ""
        # dup_strings = sorted(found, key=lambda x:x[1]-x[0])
        # last_ele = dup_strings[-1]
        # longest_dup_substring = S[last_ele[0]:last_ele[1]]
        # print(f"longest dup substring is {longest_dup_substring}")
        # return longest_dup_substring


if __name__ == "__main__":
    s=Solution()
    s.longestDupSubstring("abcd")

