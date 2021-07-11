def celeb(G):
    n=len(G)
    u,v=0,1
    for c in range(2,n+1):
        if G[u][v]:u=c
        else: v=c
    if u==n:    c=v
    else:   c=v
    for v in range(n):
        if c==v:continue
        if G[c][v]:break
        if not G[v][c]:break
    else:
        return c
    return None

from random import randrange
n = 10 #人数

# 构造数据结构，使用二维数组
G = [[randrange(2) for i in range(10)] for i in range(10)]

c = randrange(10) # 指定一位明星
print(c)
print('zxxxxxxx')
#设置关系
for i in range(10):
    G[i][c] = True #所有人都认识明星
    G[c][i] = False #明星不认识所有人

for i in G:
    print(i)
print('zxxxxxxx')
cc = celeb(G)
print(cc)