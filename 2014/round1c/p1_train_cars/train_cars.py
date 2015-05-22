#!/usr/bin/python

import itertools
import sys

from collections import defaultdict

def solve(cars):
#  [cars, bpoints] = process(cars)
  print cars
  [cars, mult] = process2(cars)
  print cars

  total = 0
  for p in itertools.permutations(cars):
    if check(p):
      total += 1
  return mult * total % 1000000007

def check(cars):
 # ans = bool(reduce(lambda prev, curr: curr[-1] if curr[0] == prev else 0, cars, cars[0][0]))
  s = ''.join(map(lambda c: ''.join(c), cars))
  last = None
  seen = set()
  ans = 1
  for c in s:
    if c != last:
      if c in seen:
        ans = False
        break
      else:
        seen.add(c)
        last = c

#  print '%s -> %s' % (s, ans)
  return ans

def process2(cars):
  newcars = []
  for car in cars:
    last = None
    newcar = ''
    for c in car:
      if c != last:
        newcar += c
        last = c
    newcars.append(newcar)
  cars = newcars

  canos = defaultdict(list)
  rest = []
  for car in cars:
    if len(set(car)) == 1:
      canos[car[0]].append(car)
    else:
      rest.append(car)
  mult = 1
  for k in canos:
    mult *= len(canos[k])
  canos = list(canos)

  begins = defaultdict(list)
  ends = defaultdict(list)
  mids = defaultdict(list)
  for car in rest:
    begins[car[0]].append(car)
    ends[car[-1]].append(car)
    if len(car) >= 3:
      for c in xrange(1, len(car) - 1):
        mids[c].append(car)

  while True:
    for c1 in rest:
      count = 0
      for c2 in rest:
        if c1[0] == c2[-1]:
          first = c2
          second = c1
          count += 1
      if count == 1:
        joined = first + second

  return [rest, mult]

def bad():
  remove = []
  for b in begins:
    print 'b: ' + str(begins)
    print 'e: ' + str(ends)
    print b
    if len(begins[b]) != 1:
      continue
    if b in ends and len(ends[b]) == 1:
      if b in canos:
        remove.add(b)
      rest.append(ends[b][0] + begins[b][0])
      remove.append(ends[b][0])
      remove.append(begins[b][0])
      ends[b].remove(ends[b][0])
      begins[b].remove(begins[b][0])
  for r in remove:
    if r in canos: canos.remove(r)
    if r in rest: rest.remove(r)
  rest.extend(canos)


def process(cars_str):
  cars = []
  beginpoints = defaultdict(list)
  for c in cars_str:
    car = (c[0], c[-1])
    cars.append(car)
    beginpoints[car[0]].append(car)
  return [cars, beginpoints]

def main():
  lines = iter(sys.stdin.readlines())
  cases = int(lines.next())
  for case in range(cases):
    l = int(lines.next())
    cars = lines.next().split()
    print 'Case #%d: %s' % (case+1, solve(cars))

main()
