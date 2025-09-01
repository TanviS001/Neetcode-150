Time, space o(n) 

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=Counter(nums)
        buckets=[[] for i in range(0,len(nums)+1)]

        for num,freq in freq_map.items():
            buckets[freq].append(num)

        result=[]
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                result.append(num)
                if len(result)==k:
                    return result
