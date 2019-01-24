import math


def roundless(number, precision):
    """
    return the number rounded with the precision asked
    :param number: number to round
    :param int precision: precision
    :return: number rounded
    """
    return math.floor(number * (math.pow(10, precision))) / (math.pow(10, precision))
