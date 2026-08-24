class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        i have a list with nums
        return true if any value appears more than once, else return false
        i will use a dictionary
        once an element appears twice, flag true otherwise keep going,
        if it finishes without seeing a key with a frequency if 2, returns false
        '''
        dict1 = {}
        for i in nums:
            if i in dict1:
                return True
            dict1[i]=1
        return False

        