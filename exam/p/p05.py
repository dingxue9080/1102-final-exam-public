def p05(l1=[1,4,3,2,5,2], x=3):
    output_list=None
    # ↓程式區域↓
    listsmall=[]
    listbig=[]
    for i in range(0,len(list)):
        if(list[i]<num):
            listsmall.append(list[i])
        elif(list[i]>=num):
            listbig.append(list[i])
    listsmall.sort()
    output_list=listsmall+listbig
    # ↑程式區域↑
    return output_list
