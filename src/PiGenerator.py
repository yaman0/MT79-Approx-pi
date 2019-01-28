import math


class PiGenerator:
    def __init__(self):
        self.value = 0

    def SerieInvCarres(self, n):
        """
        Return the "serieinvcarres" with n depth
        :param int n: max of sum
        :return: serieinvcarres
        """
        if (n < 0):
            raise ValueError('N need to be positive')
        result = 0
        for k in range(1, n + 1):
            result += 1 / math.pow(k, 2)
        return result

    def MethodeSerieInvCarres(self, n):
        """
        Compute approach of pi with SerieInvCarres
        :param int n: depth of SerieInvCarres
        :return float: approach of pi
        """
        return math.sqrt(6 * self.SerieInvCarres(n))

    def SerieInvCarresImparis(self, n):
        """
        Return the "SerieInvCarresImparis" with n depth
        :param int n: max of sum
        :return float: serieinvcarresimparis
        """
        if (n < 0):
            raise ValueError('N need to be positive')
        result = 0
        for k in range(0, n + 1):
            result += 1 / math.pow((2 * k) + 1, 2)
        return result

    def MethodeSerieInvCarresImparis(self, n):
        """
        Compute approach of pi with SerieInvCarresImparis
        :param int n: depth of SerieInvCarresImparis
        :return float: approach of pi
        """
        return math.sqrt(8 * self.SerieInvCarresImparis(n))

    def realPi(self):
        return math.pi

    def serieRamanujan(self, n):
        """
        computed result of serieRamanujan for a depth n
        :param int n: depth
        :return: serie ramanujan for n
        """
        result = 0
        for k in range(0, n + 1):
            result += ((math.factorial(4 * k)) / (math.pow(math.factorial(k), 4))) * (
                        (1103 + 26390 * k) / math.pow((4 * 99), (4 * k)))
        return result

    def methodSerieRamanujan(self, n):
        """
        Generate Pi with the ramanujan's serie
        :param int n: depth
        :return: pi
        """
        return 1 / (((2 * math.sqrt(2)) / 9801) * self.serieRamanujan(n))
