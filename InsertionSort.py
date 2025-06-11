## -------------------- InsertionSort -------------------- ##
#Written by: Aarni Junkkala
def InsertionSort(list):
    for i in range(1,len(list)): #Proses is repeated to all but first
        for k in range(i,0,-1):
            if list[k] < list[k-1]:
                list[k],list[k-1] = list[k-1],list[k]
            else:
                break
    return list

if __name__ == '__main__':
    import SortingBase as SB
    Array = SB.Generate(10)
    print("Start: " + str(Array))
    Array = InsertionSort(Array)
    print("End: " + str(Array))