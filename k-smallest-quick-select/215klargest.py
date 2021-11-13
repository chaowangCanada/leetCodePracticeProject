import heapq
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    left, right = 0, len(nums) - 1

    def partition(l, r):
        # the partition function from Quick Sort
        # https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
        pivot = l
        while l < r:
            while l <= r and nums[l] >= nums[pivot]:
                l += 1
            while l <= r and nums[r] <= nums[pivot]:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        nums[r], nums[pivot] = nums[pivot], nums[r]
        return r

    while True:
        # we only focus on one half
        # where the Kth element is
        p = partition(left, right)
        if p == k - 1:
            return nums[p]
        if p > k - 1:
            right = p - 1
        else:
            left = p + 1


if __name__ == '__main__':
    # Create a graph given in the above diagram
    print(findKthLargest([3,2,1,5,6,4], 2))
