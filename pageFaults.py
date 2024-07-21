from collections import deque

def pageFaults(pages, capacity):
  s = set()
  indexes = deque()
  page_faults = 0
  for i in range(len(pages)):
    if len(s) < capacity:
      if pages[i] not in s:
        s.add(pages[i])
        page_faults += 1
        indexes.append(pages[i])
    else:
      if pages[i] not in s:
        val = indexes.popleft()
        s.remove(val)
        s.add(pages[i])
        indexes.append(pages[i])
        page_faults += 1
      else:
        indexes.remove(pages[i])
        indexes.append(pages[i])

  return page_faults

pages = [5, 0, 1, 3, 2, 4, 1, 0, 5]
capacity = 4
print(pageFaults(pages, capacity))
