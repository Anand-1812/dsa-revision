from typing import List

def findComb(idx: int, target: int, nums: List[int], ans: List[List[int]], ds: List[int]):
    if target == 0:
        ans.append(ds.copy())
        return
    
    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i-1]:
            continue
        if nums[i] > target:
            break
        ds.append(nums[i])
        findComb(i+1, target-nums[i], nums, ans, ds)
        ds.pop()


def combSum2(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    ans = []
    ds = []
    findComb(0, target, nums, ans, ds)
    return ans

output = combSum2([10, 1, 2, 7, 6, 1, 5], 8)
print(output)
