import math


def binary_search(array, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(array) == 0:
        return -1
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def divide(self, dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """


def truncate(aInt):
    if aInt > 0:
        return math.floor(aInt)
    else:
        return math.ceil(aInt)



if __name__ == '__main__':
    v = binary_search([1, 3, 5, 7, 9], 7)
    print(truncate(-3.5))
