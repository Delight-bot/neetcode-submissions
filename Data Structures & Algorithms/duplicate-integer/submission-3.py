class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        once you come across a value that has been seen, flag it!

        found = set(nums)
        return len(found)!=len(nums)

        soln 1:
        # map, put every element, if any element gets a freq of 2 then return True
        
        found = {}
        for i in (nums):
            if i in found:
                found[i]+=1
            else:
                found[i]=1
        
        for keys,vals in found.items():
            if vals>1:
                return True
        return False
        '''
        # instead of making the hash map, use the frequencies to flag earlier

        found = {}

        for i in (nums):
            if i in (found):
                return True
            else:
                found[i]=1
        return False
        
            




        