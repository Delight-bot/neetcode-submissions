class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use a dictionary
        #if they have the same length, then they are anagrams
        #Plan: dictt and dicts:

        if len(t)!= len(s):
            return False

        dicts,dictt={},{}

        for i in range(len(s)):
            dicts[s[i]] = 1 + dicts.get(s[i],0)
            dictt[t[i]] = 1 + dictt.get(t[i],0)

        return dictt==dicts          

        


        