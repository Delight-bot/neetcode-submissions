class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        use a set
        keep the first element of the set
        add it to every element that gets into set ?? == target
        dict:
        key: actual integer, value: actual index
        '''
        # enumerate
        dict1 = {}
        for i in range(len(nums)):
            difference = target -nums[i]
            if difference in dict1:
                return [dict1[difference],i]
            dict1[nums[i]]=i
        return []



            




            
        