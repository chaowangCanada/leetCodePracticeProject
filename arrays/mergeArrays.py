def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    a = merge_wrapper(nums1, m, nums2, n)
    nums1[:] = a

def merge_wrapper(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    if n > 0 and m > 0:
        nums1 = nums1[m:] + nums1[0:m]
    i, j = n, 0
    while j < n and i < m +n:
        if nums1[i] >= nums2[j]:
            nums1[i - n +j] = nums2[j]
            j += 1
        else:
            swap(nums1, i , i - n +j)
            i += 1
    while j < n:
        nums1[m + j ] = nums2[j]
        j += 1
    return nums1

#
# def merge(nums1, m, nums2, n):
#     end = m+n-1
#     end1 = m -1
#     end2 = n -1
#
#     while(end2 >= 0):
#         if(end1 >=0):
#             nums1[end--] = nums1[end1] > nums2[end2] ? nums1[end1--] : nums2[end2--]
#         else:
#             nums1[end--] = nums2[end2--]
#


def swap(nums1, index1, index2):
    x = nums1[index1]
    nums1[index1] = nums1[index2]
    nums1[index2] = x

# [1,2,7,3,0,0]
# [1,2,5,3,7,0]
nums1 = [4,0,0,0,0,0]
nums2 = [1,2,3,5,6]
m = 1
n = 5

merge(nums1, m, nums2, n)
print(nums1)