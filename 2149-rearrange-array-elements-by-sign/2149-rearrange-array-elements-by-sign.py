class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[]
        n=[]
        for x in nums:
            if x>0:
                p.append(x)
            else:
                n.append(x)
        result = []

        for i in range(len(p)):
            result.append(p[i])
            result.append(n[i])

        return result        
