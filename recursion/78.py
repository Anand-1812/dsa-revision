from typing import List

nums = [1, 2, 3]

def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    subset_count = 1 << n
    ans = []

    for i in range(subset_count):
        current = []
        for j in range(n):
            if i & (1 << j):
                current.append(nums[j])
        ans.append(current)

    return ans

ans = subsets(nums)
print(ans)

