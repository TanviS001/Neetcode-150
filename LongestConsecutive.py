# o(n) space and time
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0

        for i in nums:
            if i-1 not in nums:
                length=0
                while i+length in nums:
                    length+=1
                longest=max(longest,length)
                
        return longest
