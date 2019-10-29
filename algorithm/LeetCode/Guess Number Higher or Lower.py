class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # left , right = 1, n
        # while left<right:
        #     piovt = left+ (right-left)//2
        #     print piovt
        #     num = guess(piovt)
        #     if num == 0:
        #         return piovt
        #     if num > 0:
        #         right = piovt - 1
        #     else:
        #         left = piovt +1
        # return left
        i = 1
        j = n
        while i < j:
            mid = (i+j) / 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                j = mid
            else:
                i = mid+1
        return i