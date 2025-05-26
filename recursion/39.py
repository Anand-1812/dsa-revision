from typing import List

def findCombination(idx: int, target: int, arr: List[int], ans: List[List[int]], comb: List[int]):
    if idx == len(arr):
        if target == 0:
            ans.append(comb.copy())  # copy to avoid mutable issues
        return

    if arr[idx] <= target:
        comb.append(arr[idx])
        findCombination(idx, target - arr[idx], arr, ans, comb)
        comb.pop()  # backtrack

    findCombination(idx + 1, target, arr, ans, comb)

def combinationSum(arr: List[int], target: int) -> List[List[int]]:
    ans = []
    comb = []
    findCombination(0, target, arr, ans, comb)
    return ans

output = combinationSum([2, 3, 6, 7], 7)
print(output)

