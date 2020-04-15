import numpy as np
import sys

coins = [1,5,10,25]
calls = 0
reads = 0

''' Making Change recursively using the recurrence in the slides '''
def mkChangeDC(n, c):
   global calls
   return 0

''' Making Change recursively avoiding the loop in mkChangeDC
    Based on a different recurrence
'''
def mkChangeDC1(n, c):
   global calls
   return 0

''' Dynamic Programming version of mkChangeDC '''
def mkChangeDP(n):
   global reads
   return 0

''' Dynamic Programming version of mkChangeDC1 '''
def mkChangeDP1(cap):
   global reads
   return 0

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
   # np.savetxt('dataDC', dataDC, delimiter=',', fmt='%d') 

   print("dataDC1:",dataDC1)
   # np.savetxt('dataDC1', dataDC1, delimiter=',', fmt='%d')

   print("dataDP:", dataDP)
   # np.savetxt('dataDP', dataDP, delimiter=',', fmt='%d')

   print("dataDP1:",dataDP1)
   # np.savetxt('dataDP1', dataDP1, delimiter=',', fmt='%d')
