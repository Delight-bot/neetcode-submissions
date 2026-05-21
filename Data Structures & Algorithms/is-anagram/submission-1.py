class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use a dictionary
        #if they have the same length, then they are anagrams
        #Plan: dictt and dicts:

        dictt={}
        dicts={}

        for i in s:
            if i not in dicts:
                dicts[i]=1 
            else:
                dicts[i]+=1
        
        for j in t:
            if j not in dictt:
                dictt[j]=1 
            else:
                dictt[j]+=1

        return dicts==dictt
           

        


        