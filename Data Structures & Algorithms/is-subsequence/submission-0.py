class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_len = len(s)
        s_len = len(t)
        i = 0
        j = 0

        while((i < sub_len) and (j < s_len)):
            if s[i] == t[j]:
                i = i + 1
            j = j + 1

        if i == sub_len:
            return True
        return False