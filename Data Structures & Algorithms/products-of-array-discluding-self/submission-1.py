class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [1]*n
        
        # first pass
        prefix = 1
        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]
    
        # second pass
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i]*=suffix
            suffix*=nums[i]

        return res

        '''
        fighting, im literally sleep deprived lol
        nums has integers
        return an array output 
        so, if we are standing at i, we dont use it in the product
        what if i use a dictionary and every element becomes a key and 
        its value is a total of the other elements
        doesnt work, how do i skip the current i
        or at every i, i can add up everything and subtract i's value
        if i have this: [1,2,4,6]
        how do i get the product excluding 1: 1x2x4x6 = 48, and if i is 
        pointing at 4, 1x2x6 = 12. 48 /4 = 12
        nums=[-1,0,1,2,3]
        
        #dict1 = {}
        lst = []
        for i in range(len(nums)):
            if nums[i]!=0:
                product = int(math.prod(nums)/nums[i])
                lst.append(product)
            else:
                product = int(math.prod(nums[:i])* math.prod(nums[i+1:]))
                lst.append(product)
        return lst
        '''

        