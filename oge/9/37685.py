s = "ABEDC BE CDG DFG EF GHF FH H "
d = {i[0]:i[1:] for i in s.split()}

f = lambda a, b: (a == b) +\
      sum(f(c, b) for c in d[a])

print(f('A', 'H'))