## -------------------- Cocktail shaker sort -------------------- ##
#Written By: Aarni Junkkala

import SortingBase as SB

def CocktailShakerSort(L):
    num = 0
    top = len(L) - 1
    bot = 0
    direction = 1
    while bot != top:
        if direction == 1: #Top
            if L[num] > L[num +1]: #If left values is greater, then swap them
                L[num],L[num+1] = L[num+1],L[num]
        if direction == -1: #Bottom
            if L[num] < L[num - 1]: #If left value is greater, then swap them
                L[num],L[num - 1] = L[num - 1],L[num]
        
        #Num is changed towards direction
        num += direction
        
        #Limiters
        if direction == 1 and num >= top:
            top -= 1
            direction = -1
            num -= 1
        elif direction == -1 and num <= bot:
            bot += 1
            direction = 1
            num += 1
        
    return L

if __name__ == '__main__':
    Array = SB.Generate(10)
    print("Start: " + str(Array))
    Array = CocktailShakerSort(Array)
    print("End: " + str(Array))