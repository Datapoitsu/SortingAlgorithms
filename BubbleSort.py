## -------------------- Bubble sort -------------------- ##
#Written By: Aarni Junkkala
import SortingBase as SB
import random

def BubbleSort(L):
    num = 0 #Index number
    top = len(L) - 1 #once this is reached, then start from bottom
    while top != 0:        
        if L[num] > L[num +1]: #If left values is greater, then swap them
            L[num],L[num+1] = L[num+1],L[num]
        
        #Increases index value and limits it to be always one less than last index
        num += 1
        if num >= top:
            num = 0
            top -= 1

if __name__ == '__main__':
    Array = SB.Generate(5)
    print("Start: " + str(Array))
    Array = BubbleSort(Array)
    print("End: " + str(Array))