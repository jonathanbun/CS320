import numpy as np
import sys
import math

coins = [1,5,10,25]
calls = 0
reads = 0


''' Making Change recursively using the recurrence in the slides '''
def mkChangeDC(n, c):
   global calls
   calls += 1
   if c==0:
      return 1
   sum = 0
   for x in range(0, (n//coins[c]) + 1):
      temp = coins[c] * x
      sum += mkChangeDC(n-temp, c-1)
   return sum

''' Making Change recursively avoiding the loop in mkChangeDC
    Based on a different recurrence
'''
def mkChangeDC1(n, c):
   global calls
   calls+=1
   if c==0:
      return 1
   if n<0:
      return 0
   if n==0:
      return 1
   sum = mkChangeDC1(n - coins[c], c)
   sum1 =  mkChangeDC1(n, c-1)
   return sum + sum1

''' Dynamic Programming version of mkChangeDC '''
def mkChangeDP(n):
   global reads
   table = [[0 for x in range(len(coins))] for x in range(n)]

   for i in range(len(coins)):
      table[0][i] = 1

   for i in range(0, n):

      for j in range(0, len(coins)):
         reads += 2
         table[i][j] = table[i-coins[j]][j] + table[i][j-1]






   return table[n - 1][len(coins) - 1]


''' Dynamic Programming version of mkChangeDC1 '''
def mkChangeDP1(n):
   global reads
   table = [[0 for x in range(len(coins))] for x in range(n)]

   for i in range(len(coins)):
      table[0][i] = 1

   for i in range(1, n):
      for j in range(len(coins)):
         if i - coins[j] >= 0:
            x = table[i - coins[j]][j]
            reads += 1
         else:
            x = 0
         if j >= 1:
            y = table[i][j - 1]
            reads += 1
         else:
            y = 0
         table[i][j] = x + y

   return table[n - 1][len(coins) - 1]

if __name__ == "__main__":
   c = len(coins)-1
   print()
   print("Making change with coins:", coins)

   # performance data: [[n, complexity], ... ]
   dataDC  = []
   dataDC1 = []
   dataDP  = []
   dataDP1 = []

   for n in range(200,2001,200):
      print()
      print("Amount:",n)

      calls = 0
      ways = mkChangeDC(n,c)
      print("DC", ways, calls)
      dataDC.append([n,calls])

      calls = 0
      ways = mkChangeDC1(n,c)
      print("DC1", ways, calls)
      dataDC1.append([n,calls])

      reads = 0
      ways = mkChangeDP(n+1)
      print("DP", ways, reads)
      dataDP.append([n,reads])

      reads = 0
      ways = mkChangeDP1(n+1)
      print("DP1", ways, reads)
      dataDP1.append([n,reads])

   #uncomment below lines to save the files for your analysis
   print("dataDC:", dataDC)
   np.savetxt('dataDC', dataDC, delimiter=',', fmt='%d')

   print("dataDC1:",dataDC1)
   np.savetxt('dataDC1', dataDC1, delimiter=',', fmt='%d')

   print("dataDP:", dataDP)
   np.savetxt('dataDP', dataDP, delimiter=',', fmt='%d')

   print("dataDP1:",dataDP1)
   pnp.savetxt('dataDP1', dataDP1, delimiter=',', fmt='%d')
