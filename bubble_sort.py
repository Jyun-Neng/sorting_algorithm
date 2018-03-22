import numpy as np

def bubble_sort(num):
    """
    Bubble sort algorithm. 
    Input: number sequence
    Output: number sequence (ascending order)
    Complexity: Worst-case O(n^2), Best-case O(n)
    """
    size = len(num)
    swapped = True 
    for i in range(size):
        if swapped is not True: 
            return num
        swapped = False
        for j in range(size-i-1):
            if num[j] > num[j+1]:
                swapped = True
                num[j], num[j+1] = num[j+1], num[j]
    return num

if __name__ == '__main__':
    low, high, size = 0, 100, 20
    num = np.random.randint(low, high, size)
    print('----before sort----')
    print(num)
    sorted_num = bubble_sort(num)
    print('----after sort----')
    print(sorted_num)
