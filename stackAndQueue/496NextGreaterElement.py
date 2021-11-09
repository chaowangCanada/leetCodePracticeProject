# First, explain the original problem of Next Greater Number: give you an array,and return an array of equal length.The corresponding index stores the next larger element, if there is no larger element, store -1. It's not easy to explain clearly in words. Let's take a direct example:
# Give you an array [2,1,2,4,3],and you return an array [4,2,4,-1,-1].
from typing import List


def nextGreaterElement(self, nums: List[int]) -> List[int]:
    output = [-1 for _ in nums]
    stack = []
    for i in range(len(nums)-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            output[i] = stack[-1]
        stack.append(nums[i])
    return output


if __name__ == '__main__':
    print(nextGreaterElement(None, [73,74,75,71,69,72,76,73]))

