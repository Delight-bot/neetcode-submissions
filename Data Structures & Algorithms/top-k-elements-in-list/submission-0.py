class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums, and k -->7
        # return the 7 most frequent elements in nums

        '''
        dict
        key               :     value
        unique element          frequency of elements

        output

        list of the elements whose freq == k

        '''
        dict1 ={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        #list comprehension??
        sorted_list = sorted(dict1.items(),key= lambda x:x[1],reverse=True)
        result = [j[0] for j in sorted_list[:k]]

        return result


        '''
        list1 =[key for key,value in dict1.items() if value==k]
        '''

        