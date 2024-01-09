## -------------------- Bubble sort -------------------- ##
#Written By: Aarni Junkkala

#Bubblesort in the best way that I was able to do it.
#If two elements weren't changed in the end, then they are in the correct place

def BubbleSort(L):
    Counter = len(L) - 1
    while Counter > -1: #Loops the list from end to start
        NotSwapped = 0
        for j in range(Counter): #Another loop from start to last loop
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                NotSwapped = 0
            else:
                NotSwapped += 1
        Counter -= 1 + NotSwapped
    return L

if __name__ == '__main__':
    import SortingBase as SB
    Array = SB.Generate(5)
    print("Start: " + str(Array))
    Array = BubbleSort(Array)
    print("End: " + str(Array))