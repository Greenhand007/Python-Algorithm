
def ins_sort(seq):
    for i in range(1,len(seq)):
        j=i
        while j>0 and seq[j-1] > seq[j]:
            seq[j-1],seq[j]=seq[j],seq[j-1]
            j-=1
    return seq


a=[5,4,3,2,1,6]


print(ins_sort(a))