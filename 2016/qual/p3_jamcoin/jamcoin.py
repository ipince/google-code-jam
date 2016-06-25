#!/usr/bin/python

import math
import itertools

def solve(n, j):
  found = []
  it = itertools.product('01', repeat=n)
  for i in it:
    if i[0] != '1' or i[-1] != '1':
      continue
    i = ''.join(i)
    common_divisors = []
    passed = True
    for base in xrange(2, 11):
      based = int(i, base)
      divs = proper_divisors(based)
      if len(divs) > 0:
        common_divisors.append(str(divs[0]))
      else:
        #print "    breaking"
        passed = False
        break
      #print "%s in base %d is %d. divisors are %s. common divs are %s" % (i, base, int(i, base), divs, common_divisors)
    if passed:
      #print "============ found!!!!!!!! ============"
      found.append(str(i) + ' ' + ' '.join(common_divisors))
    if len(found) == j:
      return found
      #print "yaayyyy: %s" % (found)

def memoize(f):
  class memodict(dict):
    def __missing__(self, key):
      ret = self[key] = f(key)
      return ret
  return memodict().__getitem__

def divisors(n):
  return [d for d in xrange(1, n) if n % d == 0]

@memoize
def proper_divisors(n):
  return list(sum([ (d, n / d) for d in xrange(2, int(math.sqrt(n)) + 1) if n % d == 0], ()))





solution = solve(16, 50)
print 'Case #1:'
for line in solution:
  print line
