class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_found=False 
       
        d={}
        for i in range(0,len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
                    
        for k,v in d.items():   #t.c=o(n),s.c=0(n)
            if v>1:
                is_found=True
                break
    
        return is_found   