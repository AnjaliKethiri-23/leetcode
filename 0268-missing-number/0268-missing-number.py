class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum=0
        # l=len(nums)
        # r=(l*(l+1))//2
        # for i in nums:
        #     sum+=i
        # return r-sum    
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i

        
