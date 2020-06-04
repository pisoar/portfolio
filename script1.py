import random
N=int(input('%:'))
L=[]
for i in range(101):
    l=['.' for i in range(101)]
    L.append(l)
TS=[]
for i in range(N):
    t=random.randrange(0,100)
    s=random.randrange(0,100)
    while (t,s) in TS:
        t=random.randrange(0,100)
        s=random.randrange(0,100)
    TS.append((t,s))
    L[t][s]='#'

a=random.randrange(0,100)
b=random.randrange(0,100)

ax=a
x=1
if L[0][ax]=='#' or a==b:
    print('ok')
else:
    k=100/(a-b)
    for i in range(100):
        ax-=1/k
        if x%k==0 and ax>=0 and ax<=100:
            if L[x][int(ax)]=='#':
                print('ok')
                break
            else:
                if x==100:
                    print('failure')
                    x+=1
        elif ax<0 or ax>100:
            print('failure')
            break
        else:
            if x==100:
                print('failure')
            x+=1
