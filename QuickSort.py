## -------------------- Quicksort -------------------- ##
#Written By: Aarni Junkkala
def Quicksort(list):
    if len(list) <= 1:
        return list
    pivot = list[-1]
    smaller, greater = [],[]

    for i in range(len(list) - 1):
        if list[i] < pivot:
            smaller.append(list[i])
        else:
            greater.append(list[i])
    return Quicksort(smaller) + [pivot] + Quicksort(greater)

if __name__ == "__main__":
    import SortingBase as SB
    Array = SB.Generate(10)
    print("Start: " + str(Array))
    Array = Quicksort(Array)
    print("End: " + str(Array))