## -------------------- Bogo sort -------------------- ##
#Written By: Aarni Junkkala
import SortingBase as SB
import random
def BogoSort(L):
    while SB.Check(L) == False:
        for i in range(len(L)):
            num = random.randint(0,len(L) - 1)
            L[num],L[i] = L[i],L[num]
    return L
    
if __name__ == '__main__':
    Array = SB.Generate(10)
    print("Start: " + str(Array))
    Array = BogoSort(Array)
    print("End: " + str(Array))
