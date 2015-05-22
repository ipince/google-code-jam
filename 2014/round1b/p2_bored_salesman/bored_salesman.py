#!/usr/bin/python

import sys
import itertools

from collections import defaultdict

def solve(zips, flights):
#  print zips
#  print flights
  perms = itertools.permutations(zips)

  scores = []
  for p in perms:
    #print "attempting " + str(p)
    route = attempt(flights, list(p))
    if route:
#      print "found route: " + str(route) + " for attempt " + str(p)
      scores.append(''.join([zips[k] for k in route]))
  return min(scores)

def attempt(flights, order):
  start = order.pop(0)
  route = [start]
  place = [start]
  while place:
    if not order:
      return route
    place = follow(flights, order, route, place)
  return None

def follow(flights, order, route, place):
  # place is a stack of where we are right now
  desired = order.pop(0)
  while place:
    if desired in flights[place[-1]]:
      # go to desired
      route.append(desired)
      place.append(desired)
      return place
    else:
      # go back and try again, until done
      place.pop()

  # couldn't make it
  return None

def main():
  lines = iter(sys.stdin.readlines())
  cases = int(lines.next())
  for case in range(cases):
    [N, M] = map(int, lines.next().split())
    zips = {}
    for i in xrange(N):
      zips[i + 1] = lines.next().replace('\n', '')
    flights = defaultdict(list)
    for _ in xrange(M):
      (i, j) = map(int, lines.next().split())
      flights[i].append(j)
      flights[j].append(i)
    print 'Case #%d: %s' % (case+1, solve(zips, flights))

main()
