class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        2 numbers that add up, you are given the total, so look for the 2 numbers that add up to taht one
        '''
        dict1 = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict1:
                return [dict1[diff],i]
            dict1[nums[i]]=i
        return []


        