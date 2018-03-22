import numpy as np


def insertionSort(num_seq):
    """
    Insertion sort algorithm.
    Input: number sequence
    Output: number sequence (ascending order)
    Complexity: O(n^2)
    """
    sorted_seq = []
    for num in num_seq:
        size = len(sorted_seq)
        for j in range(size):
            if num < sorted_seq[j]:
                num, sorted_seq[j] = sorted_seq[j], num
        sorted_seq.append(num)
    return np.asarray(sorted_seq)


if __name__ == '__main__':
    low, high, size = 0, 100, 20
    num_seq = np.random.randint(low, high, size)
    sorted_seq = insertionSort(num_seq)
    print('----before sort----')
    print(num_seq)
    print('----after sort----')
    print(sorted_seq)
