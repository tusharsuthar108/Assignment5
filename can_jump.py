def can_jump(nums):
  farthest_reach = 0
  for i, jump in enumerate(nums):
    if i > farthest_reach:
      return False
    farthest_reach = max(farthest_reach, i + jump)
  return farthest_reach >= len(nums) - 1

nums = [2, 3, 1, 1, 4]
print(can_jump(nums))
