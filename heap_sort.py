import numpy as np


def maxHeapify(heap, i, heap_size):
    """
    Compare parent and its children iteratively. 
    """
    l = 2 * i + 1
    r = 2 * (i + 1)
    if l < heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and heap[r] > heap[largest]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        maxHeapify(heap, largest, heap_size)


def buildMaxHeap(heap):
    """
    Build a max heap that each parent is larger than children. 
    """
    for i in reversed(range(len(heap) // 2)):
        maxHeapify(heap, i, len(heap))


def heapSort(heap):
    """
    Heap sort algorithm.
    Input: number sequence
    Complexity: O(nlgn)
    """
    buildMaxHeap(heap)
    heap_size = len(heap)
    for i in reversed(range(1, len(heap))):
        heap[0], heap[i] = heap[i], heap[0] # exchange the largest element with the last element
        heap_size -= 1
        maxHeapify(heap, 0, heap_size)  # make root be the largest element


if __name__ == '__main__':
    low, high, size = 0, 20, 13
    num_seq = np.random.randint(low, high, size)
    print('----number sequence----')
    print(num_seq)
    print('----build heap----')
    heapSort(num_seq)
    print(num_seq)
