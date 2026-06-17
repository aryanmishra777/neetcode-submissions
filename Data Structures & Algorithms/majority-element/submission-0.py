from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach - 1 Frequency Array
        c = Counter(nums)
        for i in c:
            if c[i] > (len(nums) // 2):
                return i
        