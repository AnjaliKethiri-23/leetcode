class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while (num>=10):
            sum=0
            while num>0:
                tem=num%10
                sum+=tem
                num//=10
            num=sum
        return num     
        