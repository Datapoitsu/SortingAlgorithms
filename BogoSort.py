## -------------------- Bogo sort -------------------- ##
#Written By: Aarni Junkkala

import SortingBase as SB
import random

def BogoSort(L):
    while SB.Check(L) == False:
        num1 = random.randint(0,len(L) - 1)
        num2 = random.randint(0,len(L) - 1)
        L[num1],L[num2] = L[num2],L[num1]
    
if __name__ == '__main__':
    Array = SB.Generate(10)
    BogoSort(Array)
    print(Array)