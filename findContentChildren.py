def findContentChildren(g, s):
  g.sort()
  s.sort()

  child_i = 0
  cookie_j = 0
  content_children = 0

  while child_i < len(g) and cookie_j < len(s):
    if s[cookie_j] >= g[child_i]:
      content_children += 1
      child_i += 1
    cookie_j += 1

  return content_children

g = [1, 2, 3]
s = [1, 1]
result = findContentChildren(g, s)
print("Maximum content children:", result)
