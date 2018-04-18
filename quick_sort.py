import numpy as np


def partition(num_seq, first, last):
    """
    Set the last element a pivot, 
    then compare with other elements.
    """
    pivot = num_seq[last]
    i = first - 1
    for j in range(first, last):
        if num_seq[j] <= pivot:
            i += 1
            num_seq[i], num_seq[j] = num_seq[j], num_seq[i]
    num_seq[i + 1], num_seq[last] = pivot, num_seq[i + 1]
    return i + 1


def quickSort(num_seq, first, last):
    """
    Quick sort algorithm.
    Input: number sequence, first index, last index
    Complexity: Worst-case is O(n^2), average-case is O(nlgn)
    """
    if first < last:
        pos = partition(num_seq, first, last)
        # the element at pos in the number sequence has been sorted
        quickSort(num_seq, first, pos - 1)
        quickSort(num_seq, pos + 1, last)


if __name__ == '__main__':
    low, high, size = 0, 100, 50
    num_seq = np.random.randint(low, high, size)
    print('----before sort----')
    print(num_seq)
    quickSort(num_seq, 0, size - 1)
    print('----after sort----')
    print(num_seq)
