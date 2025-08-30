# With O(n^2) complexity

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

# with O(n) complexity

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num]=i
