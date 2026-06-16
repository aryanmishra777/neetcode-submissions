class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find the minimum length to set the boundary for comparison
        min_len = min(len(s) for s in strs)
        
        prefix = ""
        for i in range(min_len):
            # Check the character at index 'i' across all strings
            char_to_match = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j] [i] != char_to_match:
                    return prefix  # Mismatch found, return what we have so far
            
            prefix += char_to_match  # All characters matched, append and continue
            
        return prefix # Reached the end of the shortest string, return the full prefix