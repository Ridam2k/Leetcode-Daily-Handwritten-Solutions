from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)

        xor_1 = 0
        xor_2 = 0

        if len2 % 2 !=0:
            for i in range(len1):
                xor_1 = xor_1^nums1[i]
        
        if len1 % 2 != 0:
            for i in range(len2):
                xor_2 = xor_2^nums2[i]
        
        return xor_1^xor_2