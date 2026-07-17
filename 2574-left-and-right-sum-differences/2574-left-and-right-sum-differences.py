class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        left=0
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]                                       #2574-->leetcode
        for i in range(len(nums)):
            x=abs(left-(sum-nums[i]-left))
            res.append(x)
            left+=nums[i]
        return res