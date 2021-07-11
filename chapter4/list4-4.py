def sel_sort(seq):
    for i in range(len(seq)-1,0,-1):
        max_j=i
        for j in range(i):
            if seq[j]>seq[max_j]:max_j=j
        seq[i],seq[max_j]=seq[max_j],seq[i]
    return seq

a=[5,4,3,2,1,6]
print(sel_sort(a))