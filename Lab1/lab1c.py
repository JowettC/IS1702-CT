def gcd_c(x, y):
  while y != 0:
      t = y
      y = x % y
      x = t
  return x

