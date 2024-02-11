class Solution:
    def mySqrt(self, x:int):
        """
        :type x: int
        :rtype: int
        """
        self.x = x

        if x>10:
            return sqrt(x)