def factorielle(n):
  p=1
  for k in range (1,n+1):
    p=p*k
  return p

def sommefacto(n):
  somme=0
  for k in range  (0,n+1):
    somme=somme+1/factorielle(k)
  return somme

print(sommefacto(100))
  