
mm=[[1,1,1,2,2,3,3,4,4],
    [1,1,1,1,2,2,3,4,4],
    [1,5,5,3,3,3,3,3,6],
    [7,7,5,8,3,8,9,9,6],
    [7,7,5,8,3,8,9,9,6],
    [7,7,5,8,8,8,9,6,6],
    [7,5,5,5,7,6,6,6,6],
    [7,7,7,7,7,7,6,6,6],
    [7,7,6,6,6,6,6,6,6]]
def safeMove(mv,mm):
    # adding all possible rows
    a=[i for i in range(len(mm[0]))]

    b=[]
    # removing rows where kings present
    for i in mv:
        a.remove(i[1])
        b.append(mm[i[0]][i[1]])

    # removing diagonal element of last king
    if(len(mv)>0 and mv[-1][1]-1>=0 and mv[-1][1]-1 in a):
        a.remove(mv[-1][1]-1)
    if(len(mv)>0 and mv[-1][1]+1<len(mm[0]) and mv[-1][1]+1 in a):
        a.remove(mv[-1][1]+1)

    # removing previous kings islands
    # print(b,'90000')
    i=0
    n=len(a)
    while(i<n):
        if(mm[len(mv)][a[i]] in b):
            a.remove(a[i])
            i-=1
            n-=1
        i+=1


    return a





def queen(mm,mv):
    if(len(mm[0])==len(mv)):
        print(mv)
    # print(safeMove(mv,mm),mv)
    for i in safeMove(mv,mm):
        mv.append([len(mv),i])
        queen(mm,mv)
        mv.pop()
    return

queen(mm,mv=[])