class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            piovt = left + (right - left) // 2
            num = piovt * piovt

            if num > x:
                right = piovt - 1
            elif num < x:
                left = piovt + 1
            else:
                return piovt
        return right
