def naive_celeb(G):
    n=len(G)
    for u in range(n):
        for v in range(n):
            if u==v: continue
            if G[u][v]:break
            if not G[v][u]:break
        else:
            return u
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
cc = naive_celeb(G)
print(cc)