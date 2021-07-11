def sel_sort_rec(seq,i):
    if i==0: return 
    max_j=i
    for j in range(i):
        if seq[j] >seq[max_j]:max_j=j
    seq[i],seq[max_j]=seq[max_j],seq[i]
    sel_sort_rec(seq,i-1)
    return seq

a=[5,4,3,2,1,6]
print(sel_sort_rec(a,len(a)-2))
