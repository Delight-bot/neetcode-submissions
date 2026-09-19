class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in strs:
            word = "".join(sorted(i))
            if word not in dict1:
                dict1[word] = [i]
            else:
                dict1[word].append(i)
        return list(dict1.values())