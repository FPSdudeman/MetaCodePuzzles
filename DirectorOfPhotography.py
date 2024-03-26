# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  result = 0
  p = 0
  a = 0
  b = 0
  for p in range(N):
    for a in range(N):
      if p == a:
        pass
      else:
        for b in range(N):
          if a == b:
            pass
          else:
            d1 = abs(p - a)
            d2 = abs(a - b)
            if (p - a) * (a - b) > 0 and C[p] == 'P' and C[a] == 'A' and C[b] == 'B' and X <= d1 and d1 <= Y and X <= d2 and d2 <= Y:
              result += 1
  return result
