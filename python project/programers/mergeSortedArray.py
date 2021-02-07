def MergeSortedArray(nums1, m, nums2, n):
    return sorted(nums1[:m] + nums2[:n])


print(MergeSortedArray([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
