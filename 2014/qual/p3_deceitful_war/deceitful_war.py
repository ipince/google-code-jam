#!/usr/bin/python

import sys
import copy

def war_game(naomi, ken, strat):
  naomi = copy.copy(naomi)
  ken = copy.copy(ken)
  naomi_score = 0
  while naomi:  # blocks left
    (naomi_pick, ken_pick) = strat(naomi, ken)
    if naomi_pick > ken_pick: naomi_score += 1
    naomi.remove(naomi_pick)
    ken.remove(ken_pick)
  return naomi_score

def war_round(naomi, ken):
  # blocks are sorted and nonempty
  # naomi chooses largest block
  naomi_pick = naomi[-1]
  
  # ken chooses smallest block heavier than naomi's
  choices = filter(lambda b: b > naomi_pick, ken)
  if choices:
    ken_pick = choices[0]
  else:
    ken_pick = ken[0]  # choose smallest

  return (naomi_pick, ken_pick)

def deceit_round(naomi, ken):
  # blocks are sorted and nonempty

  # if naomi's largest beats ken's largest, naomi takes the point
  # while forcing ken to choose his largest block too.
  if naomi[-1] > ken[-1]:
    return (naomi[-1], ken[-1])
  else:
    # else, ken can beat naomi no matter what she chooses. still, naomi can
    # choose smallest block, but still force ken to choose his largest.
    return (naomi[0], ken[-1])

def main():
  lines = iter(sys.stdin.readlines())
  cases = int(lines.next())
  for case in xrange(cases):
    lines.next()  # num blocks
    naomi = sorted(map(float, lines.next().split()))
    ken = sorted(map(float, lines.next().split()))
    print 'Case #%d: %d %d' % (case+1, war_game(naomi, ken, deceit_round), war_game(naomi, ken, war_round))

main()
#print war_game([0.2, 0.7], [0.3, 0.8], deceit_round)
