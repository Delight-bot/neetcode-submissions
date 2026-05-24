class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        will use a dict, a number and store its frequencies
        return a sorted list of teh frequencies and slice to 1
        '''

        dict1 = {}

        for i in (nums):
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i] = 1
        #return sorted([*dict1.keys()], reverse=True)[:k]
        return sorted([*dict1.keys()], key = lambda x: dict1[x])[-k:]