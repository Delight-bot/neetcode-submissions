class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #I dont want to use in built sort
        # Firstly:
        #if the lengths are different: Busted!
        #what if I add both strings to a set
        #What if I make the letters in the first string keys in a dictionary, 
        #if I find the same letter then give it a value one. If all the values are 1, the
        #its true
        #check = set()
        
        # dicts = {}
        # dictt = {}
        # if len(s) !=len(t):
        #     return False

        # for i in s:
        #     if i not in dicts:
        #         dicts[i]=1
        #     else:
        #         dicts[i]+=1

        # for j in t:
        #     if j not in dictt:
        #         dictt[j]=1
        #     else:
        #         dictt[j]+=1

        # if dicts==dictt:
        #     return True
        # return False

        '''

        list1 = dict1.values()
        for vals in list1:
            check.add(vals)
        return check

        if len(check)==1:
            return True
        return False

        '''
        # dictcheck = {}
        # if len(s) !=len(t):
        #     return False

        # for i in s:
        #     if i not in dictcheck:
        #         dictcheck[i]=1
        #     else :
        #         dictcheck[i]+=1
        # for j in t:
        #     if j in dictcheck:
        #         dictcheck[j]-=1
        #     else:
        #         dictcheck[j]=1

        # list1 = dictcheck.values()
        # for k in list1:
        #     if k!=0:
        #         return False
        # return True

        
        if len(s)!=len(t):
            return False

            #if the program passes the above stage , it means the strings are equal
        dicts,dictt ={},{}

        for i in range(len(s)):
            dicts[s[i]] = 1 + dicts.get(s[i],0)
            dictt[t[i]] = 1 + dictt.get(t[i],0)
        return dicts==dictt
        



            






        