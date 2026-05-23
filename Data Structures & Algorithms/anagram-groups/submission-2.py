class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        array of strings 
        all anagrams to go under one group
        use a hashmap to have a sorted word as key, then loop through
        all elements and sort, if it matches to a key(sorted), we add it as a value in
        its original form
        '''
        dict1 = {}
        for i in strs:
            look = "".join(sorted(i))

            if look not in dict1:
                dict1[look]=[i]
            else:
                dict1[look].append(i)
        
        return [*dict1.values()]