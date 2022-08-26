# Problem - https://leetcode.com/problems/find-target-indices-after-sorting-array

def targetIndices(self, nums: List[int], target: int) -> List[int]:
    if target in nums:
        first_occ, last_occ = 0, 0
        for i in nums:
            if target > i:
                first_occ += 1
            elif target == i:
                last_occ += 1

        return [i for i in range(first_occ, last_occ+first_occ)]
    return []
  
