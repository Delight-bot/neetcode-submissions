class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i have a list of words
        # I have to put anagrams in groups
        # I can make key of a group of letters using one word, then values become the 
        # words that match with that key
        # the values have to be lists

        dict1 = {}

        for i in strs:
            key = tuple(sorted(i))
            if key in dict1:
                dict1[key].append(i)
            else:
                dict1[key]=[i]
        return list(dict1.values())
        