#!/usr/bin/python

import sys

def solve(ans1, grid1, ans2, grid2):
  s1 = set(grid1[ans1 - 1])
  s2 = set(grid2[ans2 - 1])
  s = s1.intersection(s2)
  if len(s) == 0:
    return 'Volunteer cheated!'
  elif len(s) > 1:
    return 'Bad magician!'
  else:
    return list(s)[0]

lines = iter(sys.stdin.readlines())
cases = int(lines.next())
for case in range(cases):
  ans1 = int(lines.next())
  grid1 = []
  for _ in range(4):
    grid1.append(lines.next().split())
  ans2 = int(lines.next())
  grid2 = []
  for _ in range(4):
    grid2.append(lines.next().split())
  print 'Case #%d: %s' % (case+1, solve(ans1, grid1, ans2, grid2))
