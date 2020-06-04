N=int(input('タクシーの数：'))
X=int(input('移動距離（km）：'))
A=[]
B=[]
C=[]
D=[]
for i in range(N):
    a=int(input('初乗り距離（km）：'))
    b=int(input('初乗り運賃（円）：'))
    c=int(input('加算距離（km）：'))
    d=int(input('加算運賃（円）：'))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
G=[]
x=0
for i in range(N):
    if X<A[x]:#移動距離が初乗り距離未満
        G.append(B[x])
    elif X==A[x]:#移動距離が初乗り距離
        G.append(B[x]+D[x])
    else:#移動距離が初乗り距離より遠い
        f=int((X-A[x])/C[x])+1#初乗り距離以降÷加算距離、小数点以下切り捨てて１足す
        G.append(int(B[x]+f*D[x]))
    x+=1

print('最安：'+str(min(G))+'円')
print('最高：'+str(max(G))+'円')
