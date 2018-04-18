import numpy as np

def countingSort(num_seq, sorted_seq, size):
    """
    Counting sort algorithm.
    Input: number sequence, empty sequence, large number in the number sequence
    Complexity: O(k+n)
    Counting sort algorithm is not a comparison sort, so it's complexity can beats
    the lower bound of Omega(nlgn). 
    """
    cnt = [0] * size    # this size may result in memory waste
    for num in num_seq:
        cnt[num] += 1
    for i in range(1, size):
        cnt[i] += cnt[i-1]
    for num in num_seq:
        sorted_seq[cnt[num]-1] = num
        cnt[num] -= 1

if __name__ == '__main__':
    upper, size = 100, 20
    num_seq = np.random.randint(0, upper, size)
    sorted_seq = np.asarray([0] * size)
    print('----before sorted----')
    print(num_seq)
    countingSort(num_seq, sorted_seq, upper)
    print('----after sorted----')
    print(sorted_seq)
