def glcs(v,w,mat,mis,ind):
    n=len(v)
    m=len(w)
    s=[[0]*(m+1) for i in range(n+1)]
    d=[[0]*(m+1) for i in range(n+1)]
    b=[[None]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            scored=0
            if v[i-1]==w[j-1]:
                scored=d[i-1][j-1]+1
            d[i][j]=max(scored,d[i-1][j],d[i][j-1])
            
            score=0
            if v[i-1]==w[j-1]:
                score=s[i-1][j-1]+mat
            else:
                score=s[i-1][j-1]-mis
            vind=s[i-1][j]-ind
            wind=s[i][j-1]-ind
            s[i][j]=max(score,vind,wind)

            sbuf=s[i-1][j-1]+mat
            if s[i][j]==vind:
                b[i][j]="↑"
            elif s[i][j]==wind:
                b[i][j]="←"
            elif s[i][j]==sbuf:
                b[i][j]="↖︎"
    return s,d,d[n][m],b

def llcs(v,w,mat,mis,ind):
    n=len(v)
    m=len(w)
    s=[[0]*(m+1) for i in range(n+1)]
    d=[[0]*(m+1) for i in range(n+1)]
    b=[[None]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            scored=0
            if v[i-1]==w[j-1]:
                scored=d[i-1][j-1]+1
            d[i][j]=max(scored,d[i-1][j],d[i][j-1])
            
            score=0
            if v[i-1]==w[j-1]:
                score=s[i-1][j-1]+mat
            else:
                score=s[i-1][j-1]-mis
            vind=s[i-1][j]-ind
            wind=s[i][j-1]-ind
            s[i][j]=max(0,score,vind,wind)

            sbuf=s[i-1][j-1]+mat
            if s[i][j]==vind:
                b[i][j]="↑"
            elif s[i][j]==wind:
                b[i][j]="←"
            elif s[i][j]==sbuf:
                b[i][j]="↖︎"
    return s,d,d[n][m],b

def printlcs(b,v,i,j):
    index=a
    k2=['']*a
    while i > 0 and j > 0:
        if b[i][j]=="↖︎":
            k2[index-1]=v[i-1]
            i-=1
            j-=1
            index-=1
        elif b[i][j]=="↑":
            i-=1
        else:
            j-=1

#    if (i==0)&(j==0):
 #       return
  #  if b[i][j]=="↖︎":
   #     printlcs(b,v,i-1,j-1)
    #    print(v[i])
    #else:
     #   if b[i][j]=="↑":
      #      printlcs(b,v,i-1,j)
       # else:
        #    printlcs(b,v,i,j-1)
    return k2

X = "GACTAC"
Y = "CGTGAATCAT"
s,d,a,t=glcs(X,Y,5,3,4)
for i in range(0,len(X)+1):
    print(s[i])
for i in range(0,len(X)+1):
    print(t[i])
r,e,b,u=llcs(X,Y,5,3,4)
for i in range(0,len(X)+1):
    print(r[i])
for i in range(0,len(X)+1):
    print(u[i])
#k=[]
#for x in range(0,len(X)):
 #   k.append(X[x])
#k2=['']*a
#index=a
w=printlcs(t,X,len(X),len(Y))
#x=printlcs(t,Y,len(X),len(Y))
y=printlcs(u,X,len(X),len(Y))
#z=printlcs(u,Y,len(X),len(Y))
#r="".join(q)