#!/usr/bin/python3.7

import sys

def ascii(r, c):
  first = "..+" + "-+"*(c-1)
  second = "..|" + ".|"*(c-1)
  edge = "+" + "-+"*c
  cells = "|" + ".|"*c

  a = first + "\n" + second
  for i in range(r-1):
    a += "\n" + edge + "\n" + cells
  a += "\n" + edge

  return a

# Input
lines = iter(sys.stdin.readlines())
cases = int(next(lines))
for case in range(cases):
  [r, c] = map(int, next(lines).split())

  print(f"Case #{str(case+1)}:\n{ascii(r, c)}")
