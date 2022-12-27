def p09(citations=[]):
    h=None
    # ↓程式區域↓
    citations.sort()
    citations.reverse()
    for i in range(0,len(citations)):
        count=0
        h=citations[i]
        for j in range(0,len(citations)):
            if(citations[j]>=h):
                count+=1
        if(count>=h):
            break
    # ↑程式區域↑
    return h
