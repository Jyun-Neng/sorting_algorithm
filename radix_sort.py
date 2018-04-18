import numpy as np
import math


def countingSort(num_seq, sorted_seq, size, shift):
    """
    Counting sort algorithm.
    Input: number sequence, empty sequence, large number in the number sequence
    Complexity: O(k+n)
    Counting sort algorithm is not a comparison sort, so it's complexity can beats
    the lower bound of Omega(nlgn). 
    """
    cnt = [0] * size    # this size may result in memory waste
    for num in num_seq:
        num = (num >> shift) & (size - 1)
        cnt[num] += 1
    for i in range(1, size):
        cnt[i] += cnt[i - 1]
    for num in reversed(range(len(num_seq))):
        index = (num_seq[num] >> shift) & (size - 1)
        sorted_seq[cnt[index] - 1] = num_seq[num]
        cnt[index] -= 1


def radixSort(num_seq, sorted_seq, size, r):
    """
    Radix sort algorithm. 
    Sorting number sequence from first r bits to last r bits of each element.
    This algorithm must use a stable sort. 
    (i.e. order will not change after sorting e.g. counting sort)
    Complexity: big-theta((b/r)(n+2^r))
    Here we use r = lgn, so the complexity will be big-theta(bn/lgn)
    """
    upper = 2**r
    for i in range(size):
        shift = i * r
        countingSort(num_seq, sorted_seq, upper, shift)
        num_seq = np.copy(sorted_seq)


if __name__ == '__main__':
    upper, size = 100, 16
    r = int(math.log2(size))    # choose r = lgn
    b = upper.bit_length()
    d = math.ceil(b / r)        # sort d times in radix sort
    sorted_seq = np.asarray([0] * size)
    num_seq = np.random.randint(0, upper, size)
    print('----before sorted----')
    print(num_seq)
    radixSort(num_seq, sorted_seq, d, r)
    print('----after sorted----')
    print(sorted_seq)
