def reversortengineering(N,C,start,end,maxnum,minnum,res,flag):
    minval = N-1
    maxval = N*(N+1)/2-1
    if C < minval or C > maxval:
        return "IMPOSSIBLE"
    if N==0:
        if flag:
            res.reverse()
            return (res)
        return (res)

    if(C < (minval+maxval)/2):
        if res != []:
            temp = []
            for i in range( end ):
                temp.append(res.pop())
            temp.append(maxnum)
            for i in range(len(res)):
                temp.append(res.pop())
            temp.reverse()
            res = temp
        else:
            res.append(maxnum)

        return reversortengineering(N-1,C-1,start,end+1,maxnum-1,minnum,res,flag)
    else:
        if res!= []:
            temp = []
            for i in range( end ):
                temp.append(res.pop())
            temp.append(minnum)
            for i in range(len(res)):
                temp.append(res.pop())
            res = temp
        else:
            res.append(minnum)
        return reversortengineering(N-1,C-N,end+1,start,maxnum,minnum+1,res,not flag)
T = int( input())
output = []
for i in range(T):
    arr = str(input())
    L = arr.split(" ")
    L = list(map(lambda x : int(x),L))
    output.append(reversortengineering(L[0],L[1],0,0,L[0],1,[],False))
    number = 1
for i in output:
    outstr = ""
    if i != "IMPOSSIBLE":
        index = 0
        for j in i:
            outstr += str(j)
            if index != len(i)-1:
                outstr += " "
                index += 1
    else:
        outstr+= i + " "
    print("Case #{0}: {1}".format(number,outstr))
    number = number +1