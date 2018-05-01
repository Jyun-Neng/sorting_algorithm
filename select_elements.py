import numpy as np


def findMax(seq):
    """
    Find maximum in the list.
    This funcion needs at most n-1 comparisons.
    """
    maximum = seq[0]
    for element in seq[1:]:
        if element > maximum:
            maximum = element

    return maximum


def findMin(seq):
    """
    Find minimum in the list. 
    This function needs at most n-1 comparisons. 
    """
    minimum = seq[0]
    for element in seq[1:]:
        if element < minimum:
            minimum = element

    return minimum


def minMax(seq):
    """
    Find maximum and minimum in the list simultaneously. 
    This function needs at most 3(n/2) comparisons.
    """
    if len(seq) % 2:
        minimum, maximum = seq[0], seq[0]
        ptr = 1
    else:
        if seq[0] > seq[1]:
            minimum, maximum = seq[1], seq[0]
        else:
            minimum, maximum = seq[0], seq[1]
        ptr = 2

    for num1, num2 in zip(seq[ptr::2], seq[ptr + 1::2]):
        if num1 > num2:
            min_tmp = num2
            max_tmp = num1
        else:
            min_tmp = num1
            max_tmp = num2

        if max_tmp > maximum:
            maximum = max_tmp
        if min_tmp < minimum:
            minimum = min_tmp

    return minimum, maximum


if __name__ == '__main__':
    low, high, size = 0, 100, 20
    seq = np.random.randint(low, high, size).tolist()
    print("number sequence = ", seq)
    print("maximum = %d" % findMax(seq))
    print("minimum = %d" % findMin(seq))
    print("min and max = ", minMax(seq))
