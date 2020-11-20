def anagrams(word, words):
  c1 = []
  out = []
  for w in word:
    c1.append(w)
  for x in words:
    c2 = []
    for y in x:
      c2.append(y)
    if sorted(c1, key=str.lower) == sorted(c2, key = str.lower):
      out.append(x)
      continue
  return(out)
    

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))