## -------------------- Cocktail shaker sort -------------------- ##
#Written By: Aarni Junkkala
def CocktailShakerSort(list, pointers = None, direction = 1):
    if pointers == None: #Building pointers.
        pointers = [0,len(list) - 1]
    if pointers[0] == pointers[1]: #Returning when whole thing is done.
        return list
    index = pointers[0] if direction == 1 else pointers[1] #Setting index based on the direction.
    while index != pointers[(direction + 1) // 2]:
        if (direction == 1 and list[index] > list[index + direction]) or (direction == -1 and list[index + direction] > list[index]):
            list[index],list[index + direction] = list[index + direction],list[index]
        index += direction
    
    pointers[(direction + 1) // 2] -= direction #Changes the pointer to be closer to the center.
    return CocktailShakerSort(list,pointers, direction * -1)

if __name__ == '__main__':
    import SortingBase as SB
    Array = SB.Generate(10)
    print("Start: " + str(Array))
    Array = CocktailShakerSort(Array)
    print("End: " + str(Array))