class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for i in range(len(s)):
            if s[i] in freq1:
                freq1[s[i]] = freq1[s[i]] + 1
            else:
                freq1[s[i]] = 1

        for i in range(len(t)):
            if t[i] in freq2:
                freq2[t[i]] = freq2[t[i]] + 1
            else:
                freq2[t[i]] = 1

        if freq1 == freq2:
            return True
        return False