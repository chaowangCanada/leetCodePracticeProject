# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.
from typing import List


def singleNonDuplicate(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 1:
            mid -= 1
        print(mid ,":", nums[mid])
        if nums[mid] == nums[mid + 1]:
            left = mid +2
        else:
            right = mid
    return nums[left]


if __name__ == '__main__':
    print(singleNonDuplicate(None, [1,1,3,3,7,7,10,11,11]))
