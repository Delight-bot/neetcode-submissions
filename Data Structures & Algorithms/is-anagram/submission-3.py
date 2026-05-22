class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        same exact characters
        return sorted(s)==sorted(t)
        use a hashmap, if the frequancy is the same number throughout, bingo
        or look at s & t at the same time, 
        '''
        found = {}
        if len(s)!=len(t):
            return False

        for i in range(len(s)):
                if s[i] not in found:
                    found[s[i]]=1
                else:
                    found[s[i]]+=1

        for j in range(len(s)):
            if t[j] in found:
                found[t[j]]-=1
                if found[t[j]]==0:
                    del found[t[j]] 
            else:
                found[t[j]]=1

        return len(found)==0
        


        

        