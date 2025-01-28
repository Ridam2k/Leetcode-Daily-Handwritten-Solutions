from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = [ (nums[i], i) for i in range(n) ]
        sorted_arr = sorted(arr, key=lambda x: x[0])
        l = 0
        r = 1

        while(r<n):
            print(l, r)
            if sorted_arr[r][0] - sorted_arr[r-1][0]  > limit:
                indices = []
                for i in range(l, r):
                    indices.append(sorted_arr[i][1])
                sorted_indices = sorted(indices)

                for idx in sorted_indices:
                    nums[idx] = sorted_arr[l][0]
                    l+=1
                
                l = r
            r+=1
        
        indices = []
        for i in range(l, r):
            indices.append(sorted_arr[i][1])
        sorted_indices = sorted(indices)

        for idx in sorted_indices:
            nums[idx] = sorted_arr[l][0]
            l+=1

        return nums
        