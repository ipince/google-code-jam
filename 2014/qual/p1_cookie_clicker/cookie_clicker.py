#!/usr/bin/python

import sys

# python doesn't have tail-recursion optimization :(
def solve_recursive(start, rate, elapsed, farm, gain, goal):
  stay = secs(start, rate, goal)
  farmtime = secs(start, rate, farm)
  buy = farmtime + secs(start, rate + gain, goal)
  if stay < buy:
    return elapsed + stay
  else:
    return solve(0, rate + gain, elapsed + farmtime, farm, gain, goal)

def solve_iterative(start, rate, elapsed, farm, gain, goal):
  while True:
    stay = secs(start, rate, goal)
    farmtime = secs(start, rate, farm)
    buy = farmtime + secs(start, rate + gain, goal)
    if stay < buy:
      return elapsed + stay
    else:
      start = 0
      rate += gain
      elapsed += farmtime

def secs(current, rate, goal):
  return (goal - current) / rate

def main():
  lines = iter(sys.stdin.readlines())
  cases = int(lines.next())
  for case in range(cases):
    [C, F, X] = map(float, lines.next().split())
    print 'Case #%d: %.7f' % (case+1, solve_iterative(0, 2.0, 0.0, C, F, X))

main()
