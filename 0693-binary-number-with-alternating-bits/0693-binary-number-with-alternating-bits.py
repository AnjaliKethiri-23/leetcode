class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=[]
        while n>0:
            b=n%2
            n//=2
            s.append(b)
        for x in range(0,len(s)-1):
            if s[x]==s[x+1]:
                return False
        return True        