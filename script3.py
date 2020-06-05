N=int(input('医師の人数：'))
m=0
T=[]
for i in range(N):
    t=int(input('各医師の一人当たりにかける診察時間（5分単位）：'))
    T.append(t)
    m+=int(180/t)#各医師の診察可能な最大患者数

C=[]
I=[]
M=[]
for i in range(m):
    check_in=str(input('M:診察、E:緊急、'))
    C.append(check_in)
    if check_in=='E':
        I.append(i)
    else:
        M.append(i)


x=0#時間
n=0#Mのうちの診察した人数
z=len(I)-N
h=N
for i in range(36):
    if x==0:
        if not len(I)==0:
                if len(I)>=N:
                    for i in range(N):
                        print(str(I[i])+'番 '+'9:00')
                else:
                    for i in range(len(I)):
                        print(str(I[i])+'番 '+'9:00')
                    for i in range(N-len(I)):
                        print(str(M[i])+'番　'+'9:00')
                        n+=1
                x+=5
        else:
            for i in range(N):
                print(str(M[i])+'番　'+'9:00')
                n+=1
            x+=5
    else:
        y=0
        for i in range(N):
            if x%T[y]==0:
                if z>0:
                    print(str(I[h])+'番　'+str(9+int(x/60))+':'+str(x%60))
                    z-=1
                    h+=1
                    y+=1
                else:
                    print(str(M[n])+'番　'+str(9+int(x/60))+':'+str(x%60))
                    n+=1
                    y+=1
            else:
                y+=1
        x+=5
