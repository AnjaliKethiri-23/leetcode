class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=min(nums)
        r=max(nums)
        gcd=1
        for i in range(1,min(s,r)+1):
            if s%i==0 and r%i==0:
                gcd=i
        return gcd        