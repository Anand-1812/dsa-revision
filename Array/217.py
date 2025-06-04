from typing import List

def containsDuplciate(nums: List[int]) -> bool:
    num_set = set()

    for n in nums:
        if n in num_set:
            return True
        num_set.add(n)
    return False

output = containsDuplciate([1, 2, 3, 1])
print(output)
