class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        return the indices of numbers that match
        array = nums
        fot stuuf in dict
        dict: key is going to be num, val is going to be the index
        '''
        dict1 = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict1:
                return [dict1[diff],i]
            else:
                dict1[nums[i]] = i
        

        