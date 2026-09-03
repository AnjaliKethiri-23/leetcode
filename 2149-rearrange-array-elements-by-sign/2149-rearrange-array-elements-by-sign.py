class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
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
    