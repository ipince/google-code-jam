
from collections import defaultdict


ZERO = 'ZERO'
ONE = 'ONE'
TWO = 'TWO'
THREE = 'THREE'
FOUR = 'FOUR'
FIVE = 'FIVE'
SIX = 'SIX'
SEVEN = 'SEVEN'
EIGHT = 'EIGHT'
NINE = 'NINE'
ALL_LETTERS = set([c for x in 'ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE'])

def solve(s):
  letters = defaultdict(int)
  for c in s:
    letters[c] = letters[c] + 1
  numbers = extract_known(letters)

  brute_force(letters)
  print letters
  return numbers

def extract_known(letters):
  zeros = extractif(letters, 'Z', ZERO)
  twos = extractif(letters, 'W', TWO)
  sixes = extractif(letters, 'X', SIX)
  eights = extractif(letters, 'G', EIGHT)
  numbers = list()
  numbers.extend([0 for i in xrange(zeros)])
  numbers.extend([2 for i in xrange(twos)])
  numbers.extend([6 for i in xrange(sixes)])
  numbers.extend([8 for i in xrange(eights)])
  return numbers

def extractif(letters, char, extract):
  count = 0
  while letters[char] >= 1:
    for c in extract:
      letters[c] = letters[c] - 1
    count += 1
  return count

def extract(letters, number_str):
  for c in number_str:
    letters[c] = letters[c] - 1

def brute_force(sofar, letters):
  if all([letters[c] == 0 for c in ALL_LETTERS]):
    # we're done!
    return sofar

  got_one_letter = False
  if has_letters_for(ONE):
    extract(letters, ONE)
    sofar.add(1)
    got_one_letter = True
  elif has_letters_for(THREE):
    extract(letters, THREE)
    sofar.add(3)
    got_one_letter = True
  elif has_letters_for(FOUR):
    extract(letters, FOUR)
    sofar.add(4)
    got_one_letter = True
  elif has_letters_for(FIVE):
    extract(letters, FIVE)
    sofar.add(5)
    got_one_letter = True
  elif has_letters_for(SEVEN):
    extract(letters, SEVEN)
    sofar.add(7)
    got_one_letter = True
  elif has_letters_for(NINE):
    extract(letters, NINE)
    sofar.add(9)
    got_one_letter = True

  # here it gets tricky. we can continue. or we fail.
  if got_one_letter:
    #brute_force()
  else:
    #try a different letter?

def has_letters_for(letters, number_str):
  return all([letters[c] > 0 for c in number_str])

print solve('ZEROTWOSIXEIGHTZERO')

