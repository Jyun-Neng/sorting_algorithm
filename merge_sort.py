import numpy as np


def merge(num_seq, first, middle, last):
    l_seq = np.copy(num_seq[first:middle + 1])
    r_seq = np.copy(num_seq[middle + 1:last + 1])
    i, j = 0, 0
    for k in range(first, last + 1):
        # Rather than append large number at the end of l_seq and r_seq,
        # I check both i and j are less than each sequence length.
        if i < len(l_seq) and j < len(r_seq):
            if l_seq[i] < r_seq[j]:
                num_seq[k] = l_seq[i]
                i += 1
            else:
                num_seq[k] = r_seq[j]
                j += 1
        elif i == len(l_seq) and j < len(r_seq):
            num_seq[k] = r_seq[j]
            j += 1
        elif j == len(r_seq) and i < len(l_seq):
            num_seq[k] = l_seq[i]
            i += 1


def mergeSort(num_seq, first, last):
    """
    Merge sort algorithm.
    Input: number sequence, first index, last index
    Complexity: O(nlgn))
    """
    if first < last:
        middle = (first + last) // 2
        mergeSort(num_seq, first, middle)
        mergeSort(num_seq, middle + 1, last)
        merge(num_seq, first, middle, last)


if __name__ == '__main__':
    low, high, size = 0, 100, 25
    num_seq = np.random.randint(low, high, size)
    print('----before sort----')
    print(num_seq)
    mergeSort(num_seq, 0, size - 1)
    print('----after sort----')
    print(num_seq)
