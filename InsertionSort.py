## -------------------- InsertionSort -------------------- ##
#Written by: Aarni Junkkala

def InsertionSort(L):
    for i in range(1,len(L)): #Proses is repeated to all but first
        holdIndex = i
        while holdIndex > 0: #Swaps smaller cards to left and greater to right.
            if L[holdIndex] < L[holdIndex - 1]:
                L[holdIndex],L[holdIndex - 1] = L[holdIndex - 1],L[holdIndex]
                holdIndex -= 1
            else:
                break
    return L


if __name__ == '__main__':
    import SortingBase as SB
    Array = SB.Generate(10)
    print("Start: " + str(Array))
    Array = InsertionSort(Array)
    print("End: " + str(Array))