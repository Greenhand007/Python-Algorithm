def ins_sort_rec(seq,i):
    if i==0:return
    ins_sort_rec(seq,i-1)
    j=i
    while j>0 and seq[j-1] > seq[j]:
        seq[j-1],seq[j]=seq[j],seq[j-1]
        j-=1
    return seq


a=[5,4,3,2,1,6]

print(ins_sort_rec(a,len(a)-1))
