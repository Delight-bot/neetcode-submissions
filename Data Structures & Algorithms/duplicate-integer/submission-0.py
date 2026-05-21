class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #if any value in the array appears twice, return True
        #Method
        #iterate and add elements to a set
        #a set can only contain unique elemnt
        #if it is already in there: busted!
        check = set()
        for i in nums:
            if i in check:
                return True
            else:
                check.add(i)
        return False

        