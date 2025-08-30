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
