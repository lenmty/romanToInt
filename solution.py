class Solution:
  def romanToInt(self, s: str) -> int:
    s = list(s)
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0

    prev = 0
    nxt = nums[s.pop(0)]

    while s:
      prev, nxt = nxt, nums[s.pop(0)]
      if nxt > prev:
        res += nxt - prev
        nxt = nums[s.pop(0)] if s else 0
      else:
        res += prev

    res += nxt
    
    return res

print(Solution().romanToInt(input()))