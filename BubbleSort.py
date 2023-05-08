## -------------------- Bubble sort -------------------- ##
#Written By: Aarni Junkkala
import SortingBase as SB
import random

def BubbleSort(L):
    num = 0 #Index number
    while SB.Check(L) == False:
        
        #print(L)
        
        if L[num] > L[num +1]: #If left values is greater, then swap them
            L[num],L[num+1] = L[num+1],L[num]
        
        #Increases index value and limits it to be always one less than last index
        num += 1
        if num >= len(L) - 1:
            num = 0

if __name__ == '__main__':
    Array = SB.Generate(10)
    BubbleSort(Array)
    print(Array)