
from math import log, sqrt

def factorielle(n):
  p=1
  for k in range (1,n+1):
    p=p*k
  return p

def sommefacto(k):
  somme=0
  for k in range  (0,k+1):
    somme=somme+1/factorielle(k)
  return somme


def ex111 (x): return 1/(log(3*x)+1)
def ex112 (x): return 
ex112 = lambda x : x/(sqrt(2*x-1))
def sommeg(debut,fin,fonction):
  somme = 0 
  for i in range(debut,fin+1):
    somme += fonction(i)
  return somme







def facto(n):
  if n==0:
    return 1
  else:
    return n*facto(n-1) 

def combi(n,p):
  somme=facto(n)/(facto(p)*facto(n-p))
  return somme


def syra(x,c):
  for c in range(0,c+1):
    if x%2 == 0 :
      x=x/2
    else:
      x=x*3+1
    print(x)

print(syra(6,12))