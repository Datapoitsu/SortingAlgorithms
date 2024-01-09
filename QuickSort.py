## -------------------- Quicksort -------------------- ##
#Written By: Aarni Junkkala

def Quicksort(L):

    if len(L) <= 1: #too short to sorted
        return L
    
    #Pivot works as division point, where rest of the numbers are separated
    #into groups of greater and smaller.
    pivot = L[0]
    
    smaller, greater = [],[]

    for i in range(1, len(L)): #Checks all but pivot and divides them into apropreate group
        if L[i] < pivot:
            smaller.append(L[i])
        if L[i] >= pivot:
            greater.append(L[i])
    #Repeats this funktion if there is something to be repeated
    if len(smaller) > 1: 
        smaller = Quicksort(smaller)
    if len(greater) > 1:
        greater = Quicksort(greater)
    
    #Returns all pieces in way where smaller parts are first, then pivot and then greater at last.
    return smaller + [pivot] + greater

if __name__ == "__main__":
    import SortingBase as SB
    Array = SB.Generate(10)
    print("Start: " + str(Array))
    Array = Quicksort(Array)
    print("End: " + str(Array))