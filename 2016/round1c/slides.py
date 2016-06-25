
def solve(b, m):
  # subtract b-1 from m until we reach it.
  if 2^(b - 2) < m:
    return ('IMPOSSIBLE', [])

  

  # for n, s(n) = n(n+1)/2 ways
  # for n+1, its 1 + 

  # n = 2
  # s(2) = 1
  # s(3) = 1 + s(2) = 2
  # s(4) = 1 + s(3) + s(2) = 4
  # s(5) = 1 + 4 + 2 + 1 = 8
  # s(6) = 16 ===> s(n) = 2^(n-2) ?

  # 01  -> slide from b1 to b2
  # 00 


# dict w wardrobe. pick outfit.
# save combos into set. save outfit into set.
# pick new outfit. if already in set, pick a new one.
# if it contains combos
