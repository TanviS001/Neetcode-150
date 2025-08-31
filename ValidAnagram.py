# Optimized Approach o(n) time complexity, o(1) space complexity 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        count=[0]*26

        for ch in s:
            count[ord(ch)-ord('a')]+=1

        for ch in t:
            count[ord(ch)-ord('a')]-=1
            if count[ord(ch)-ord('a')]<0:
                return False
        
        return True

# Naive Approach
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic={}

        for i in s:
            if i not in s_dic:
                s_dic[i]=1
            else:
                s_dic[i]+=1
        
        for i in t:
            if i not in s_dic or s_dic[i]<1:
                return False
            else:
                s_dic[i]-=1

        for i in s_dic:
            if s_dic[i]>0:
                return False
                
        return True


