def checkValidString(s):
  low = 0
  high = 0
  for c in s:
    if c == '(':
      low += 1
      high += 1
    elif c == ')':
      low -= 1
      high -= 1
    else:
      low -= 1
      high += 1
    if high < 0:
      return False
    low = max(low, 0)
  return low == 0

s = "()"
print(checkValidString(s))
