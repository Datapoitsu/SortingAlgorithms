## -------------------- Bubble sort -------------------- ##
#Written By: Aarni Junkkala

#Bubblesort in the best way that I was able to do it.
#If two elements weren't changed in the end, then they are in the correct place

def BubbleSort(list):
    Counter = len(list) - 1
    for k in range(len(list) - 1): #Loops the list from end to start
        for i in range(len(list) - 1 - k):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
    return list

if __name__ == '__main__':
    import SortingBase as SB
    Array = SB.Generate(10)
    print("Start: " + str(Array))
    Array = BubbleSort(Array)
    print("End: " + str(Array))