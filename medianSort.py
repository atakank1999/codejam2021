


def medianSort(N,next,l1):
    strout = "{0} {1} {2}".format(l1[-2], l1[-1], next)
    print(strout,flush=True)
    median = int(input())
    if median == l1[-1]:
        l1.append(next)
    elif median == next:
        l1.insert(l1.index(l1[-1]),next)
    else:
        if l1 == [1,2] and median == 1:
            l1 = [3,1,2]
        else:
            if next == 4:
                strout ="{0} {1} {2}".format(l1[0],l1[1],next)
                print(strout,flush=True)
                result = int(input())
                if result == l1[0]:
                    l1.insert(0,next)
                else:
                    l1.insert(1,next)
            else:    
                i = l1.index(l1[-3])
                while i >= 1:
                    strout = "{0} {1} {2}".format(l1[i], l1[i-1], next)
                    print(strout,flush=True)
                    result = int(input())
                    if i == 1 and result == l1[0]:
                        l1.insert(0,next)
                        break

                    if result != l1[i+1]:
                        if result == next:
                            l1.insert(i,next)
                            break
                        elif result == l1[i]:
                            l1.insert(i+1,next)
                            break
                    else:
                        i-=1
    if(next == N):
        output = ""
        for i in l1:
            output += str(i) + " "
        print(output)
        response = int(input())
        if response == 1:
            return 1
        else:
            return -1
    else:
        medianSort(N,next+1,l1)
            
params = str(input())
params = params.split(' ')
map(lambda x: int(x),params)
for i in range(int(params[0])):
    l1 = [1,2]
    medianSort(int(params[1]),3,l1)



