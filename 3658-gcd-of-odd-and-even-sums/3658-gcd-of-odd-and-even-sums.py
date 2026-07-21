class Solution(object):
    def gcdOfOddEvenSums(self, n):
        even = []
        odd = []

        for i in range(1, (n * 2) + 1):
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        s = sum(even)
        r = sum(odd)

        while r != 0:
            s, r = r, s % r

        return s