class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        array == nums
        return true if any val appears more than once
        '''
        dict1 = {}

        for i in nums:
            if i in dict1:
                return True
            dict1[i]=1
        return False
        
        
        