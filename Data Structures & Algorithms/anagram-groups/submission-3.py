class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        what do they have in common
        they have the same letters back and forth
        soln:
        hash map were the sorted word is the key and the value 
        is a list that appends the original word
        edge cases:
        if its empty return a list of empty and if its just 
        one, return a a list of whatever is in there

        eg: ["act","pots","tops","cat","tac","stop","hat"]
        {"act":["act","cat","tac"],
         "opst":[]
        
        }
        return res = [[],[],[]]
        '''
        dict1 = {}
        for i in strs:
            word = "".join(sorted(i))
            if word not in dict1:
                dict1[word] = [i]
            else:
                dict1[word].append(i)
        return list(dict1.values())

        
        