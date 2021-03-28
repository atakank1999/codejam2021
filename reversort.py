def Reversort(L):
    cost = 0
    for i in range (len(L)-1):
        minindex = L.index(min(L[i:]))
        L[i:minindex+1] = L[i:minindex+1][::-1]
        cost += minindex-i+1
    return (cost)

noOfCases = int(input())
output = []
for i in range(noOfCases):
    length = int(input())
    arr = str(input())
    L = arr.split(" ")
    L = list(map(lambda x : int(x),L))
    output.append(Reversort(L))
    
j = 1
for i in output:
    print("Case #{0}: {1}".format(j,i))
    j+=1
