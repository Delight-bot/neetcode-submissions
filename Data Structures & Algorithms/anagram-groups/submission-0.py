class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = {}
        result = []
        for i,strings in enumerate(strs):
            sorted_word = ''.join(sorted(strings))
            if sorted_word not in dict1:
                dict1[sorted_word]=[i]
            else:
                dict1[sorted_word]+=[i]
        for key in dict1:
            group = []
            for index in dict1[key]:
                group.append(strs[index])
            result.append(group)
        return result
        

        


        