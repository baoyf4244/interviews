from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        median_idx = total_len // 2
        trav_idx = 0
        max_len = max(len(nums1), len(nums2))
        i = 0
        cur = None
        pre = None

