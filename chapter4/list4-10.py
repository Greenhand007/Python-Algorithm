def topsort(G):
    count=dict((u,0) for u in G)
    for u in G:
        for v in G:
            count[v]+=1
    Q=[u for u in G if count[u]==0]
    S=[]
    while Q:
        u=Q.pop()
        S.append(u)
        for v in G[u]:
            count[v]-=1
            if count[v]==0:
                Q.append(v)
    return S