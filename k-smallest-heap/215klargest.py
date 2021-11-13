import heapq
from typing import List


def find_kth_largest(ints, k):
    # base case
    if not ints or len(ints) < k:
        exit(-1)

    # build a min-heap from the first `k` elements in the list
    pq = ints[0:k]
    heapq.heapify(pq)

    # do for remaining list elements
    for i in range(k, len(ints)):
        # if the current element is more than the root of the heap
        if ints[i] > pq[0]:
            # replace root with the current element
            heapq.heapreplace(pq, ints[i])

    # return the root of min-heap
    return pq[0]


def findKthLargest(nums: List[int], k: int) -> int:
    def heapify(i):
        """Given that the children are heaps, this function would
        convert a tree starting with this node to a heap

        Args:
            i (int): the index for the node to be heapified

        Returns: void
        """
        nonlocal heap
        if i >= len(heap):
            return

        child1 = 2 * i + 1
        child2 = 2 * i + 2
        max_i = i
        if child1 < len(heap) and heap[child1] < heap[max_i]:
            max_i = child1
        if child2 < len(heap) and heap[child2] < heap[max_i]:
            max_i = child2
        if max_i != i:
            heap[i], heap[max_i] = heap[max_i], heap[i]
            heapify(max_i)

    def push(num):
        """This function pushed new node to a heap.

        Args:
            num (int): The new element to be pushed.
        """
        nonlocal heap
        # append it to the heap first
        heap += [num]
        cur = len(heap) - 1
        par = (cur - 1) // 2
        # push it to the right place by switching it
        # with its parent
        while par >= 0 and heap[par] > heap[cur]:
            heap[cur], heap[par] = heap[par], heap[cur]
            cur = par
            par = (cur - 1) // 2

    heap = []

    for i in range(len(nums)):
        if len(heap) < k:  # before size == K
            push(nums[i])
        elif nums[i] > heap[0]:  # after size == K
            heap[0] = nums[i]
            heapify(0)
    return heap[0]


if __name__ == '__main__':
    # Create a graph given in the above diagram
    print(findKthLargest([3,2,1,5,6,4], 2))
