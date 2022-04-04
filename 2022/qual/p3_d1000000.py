#!/usr/bin/python3.7

import sys

def longest(dice):
  if len(dice) <= 4:
    return len(dice)  # pick them all

  # if more than 4.. i can pick at least 4.
  # I can pick a 5th if there's at least one >= 5
  # I can pick a 6th if i can pick
  dice = sorted(dice)
  ans = 1
  for d in dice:
    if d >= ans:
      ans += 1
  ans -= 1
  return ans

# Input
lines = iter(sys.stdin.readlines())
cases = int(next(lines))
for case in range(cases):
  n = int(next(lines))
  dice = list(map(int, next(lines).split()))

  print(f"Case #{str(case+1)}: {longest(dice)}")
