class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        a list thats n long
        create a new one called ans thats double the length of n and the 
        numbers in nums are repeated twice to make the double n
        '''
        return nums + nums
        #for i in (nums):
            #ans.append(i)