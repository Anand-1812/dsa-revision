from typing import List

def findContentChildren(g: List[int], s : List[int]) -> int:
    n = len(g)
    m = len(s)
    l = 0
    r = 0
    sorted(g)
    sorted(s)

    while (l < m and r < n):
        if (g[r] <= s[l]):
            r += 1
        l += 1

    return r

ans = findContentChildren([1, 2, 3], [1, 1])
print(ans)
