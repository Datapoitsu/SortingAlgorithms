## -------------------- Sorting base -------------------- ##
#Written By: Aarni Junkkala

#Base tools for my sorting algorithms, as there are many elements that repeat.

import random

def Generate(size): #Generates a list of wanted size
    L = []
    for i in range(1,size + 1):
        L.append(i)
    L = Shuffle(L)
    return L

def Shuffle(L):
    for i in range(len(L)):
        num = random.randint(0,len(L) - 1)
        holder = L[num]
        L[num] = L[i]
        L[i] = holder
    return(L)

def Check(L): #Checks if list is in order, proper algoritms, shouldn't need  this
    for i in range(0,len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True

def Visualize(L):
    for i in range(len(L)):
        s = ""
        for k in range(L[i]):
            s += "█"
        print(s + " " + str(L[i]))
        
if __name__ == "__main__":
    print(Generate(10))