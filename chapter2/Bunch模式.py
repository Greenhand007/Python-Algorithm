
class Bunch(dict):
    def __init__(self,*args,**kwds):
        super(Bunch,self).__init__(*args,**kwds)
        self.__dict__=self

x=Bunch(name='Jayne Cobb',position="Public Relations")
print(x.name)

T=Bunch
t=T(left=T(left='a',right='b'),right=T(left='c'))
print(t.right,t.left)

print('t.left.right -> {} '.format(t.left.right))

print("t['left']['right'] ->{}".format(t['left']['right']))

print('left' in t.right)

print('right' in t.right)