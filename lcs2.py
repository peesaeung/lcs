#import operator

def glcs(v,w,mat,mis,ind):
    n=len(v)
    m=len(w)
    s=[[0]*(m+1) for i in range(n+1)]
#    d=[[0]*(m+1) for i in range(n+1)]
    b=[['']*(m+1) for i in range(n+1)]
    
    for p in range(1,m+1):
        s[0][p]=s[0][p-1]-2
        b[0][p]="←"
    for p in range(1,n+1):
        s[p][0]=s[p-1][0]-2
        b[p][0]="↑"
    for i in range(1,n+1):
        for j in range(1,m+1):
#            scored=0
 #           if v[i-1]==w[j-1]:
  #              scored=d[i-1][j-1]+1
   #         d[i][j]=max(scored,d[i-1][j],d[i][j-1])
            
            score=0
            if v[i-1]==w[j-1]:
                score=s[i-1][j-1]+mat
            else:
                score=s[i-1][j-1]-mis
            vind=s[i-1][j]-ind
            wind=s[i][j-1]-ind
            s[i][j]=max(score,vind,wind)
    
            sbuf1=sbuf2=0
            if i>1:
                if j>1:
                    sbuf1=s[i-1][j-1]+mat
                    sbuf2=s[i-1][j-1]-mis
            scheck=max(s[i-1][j-1],s[i][j-1],s[i-1][j])
            
            if s[i][j]==vind:
                b[i][j]=b[i][j]+"↑"
            elif scheck==s[i-1][j]:
                b[i][j]=b[i][j]+'↑'
            if s[i][j]==wind:
                b[i][j]=b[i][j]+'←'            
            elif scheck==s[i][j-1]:
                b[i][j]=b[i][j]+'←'
            if scheck==s[i-1][j-1]:
                b[i][j]=b[i][j]+'↖︎'
            elif s[i][j]==sbuf1:
                b[i][j]=b[i][j]+'↖︎'
            elif s[i][j]==sbuf2:
                b[i][j]=b[i][j]+'↖︎'
    return s,b

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

            sbuf1=s[i-1][j-1]+mat
            sbuf2=score=s[i-1][j-1]-mis
            if s[i][j]==vind:
                b[i][j]="↑"
            if s[i][j]==wind:
                b[i][j]="←"
            if s[i][j]==sbuf1:
                b[i][j]="↖︎"
            elif s[i][j]==sbuf2:
                b[i][j]="↖︎"
    
    #index, value = max(enumerate(s), key=operator.itemgetter(1))
    #print (index,value)    
    return s,d,d[n][m],b

def printglcs(b,v,w,i,j):
    k2=[]
    while i > 0 and j > 0:
        if "↖︎" in b[i][j]:
            k2.insert(0,v[i-1])
            i-=1
            j-=1
            
        elif "↑" in b[i][j]:
            i-=1
        else:
            j-=1

#    if (i==0)&(j==0):
 #       return
  #  if b[i][j]=="↖︎":
   #     printlcs(b,v,i-1,j-1)
    #    k2.insert(0,v[i-1])
    #else:
     #   if b[i][j]=="↑":
      #      printlcs(b,v,i-1,j)
       # else:
        #    printlcs(b,v,i,j-1)
    return k2

def printllcs(b,v,a,i,j):
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

X1="GCATGCTA"
Y1="GATTACAA"
X2="GACTAC"
Y2="CGTGAATCAT"
print(X1,Y1)
s1,t1=glcs(X1,Y1,5,1,2)
for i in range(0,len(X1)+1):
    print(s1[i])
for i in range(0,len(X1)+1):
    print(t1[i])
s2,d2,a2,t2=llcs(X2,Y2,5,3,4)
for i in range(0,len(X2)+1):
    print(s2[i])
for i in range(0,len(X2)+1):
    print(t2[i])
#k=[]
#for x in range(0,len(X)):
 #   k.append(X[x])
#k2=['']*a
#index=a
w=printglcs(t1,X1,Y1,len(X1),len(Y1))

#y=printllcs(u,X,b,len(X),len(Y))
print(w)
#r="".join(q)