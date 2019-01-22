import math


class PiGenerator:
    def __init__(self):
        self.value = 0

    def SerieInvCarres(self,n):
        """
        Return the "serieinvcarres" with n depth
        :param int n: max of sum
        :return: serieinvcarres
        """
        if(n<0):
            raise ValueError('N need to be positive')
        result = 0
        for k in range(1, n+1):
            result += 1 / math.pow(k, 2)
        return result
