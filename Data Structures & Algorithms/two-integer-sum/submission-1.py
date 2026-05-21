class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 5 have n40s
        # There are numbers in a list and
        # eqn: target is the total total =a+b, 

        dict1 = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict1:
                return [dict1[diff],i]
            dict1[nums[i]] = i
