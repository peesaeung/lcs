def glcs(v,w,mat,mis,ind):
    s=[[0]*(len(w)+1) for i in range(len(v)+1)]
    b=[['']*(len(w)+1) for i in range(len(v)+1)] 
    for p in range(1,len(w)+1):
        s[0][p]=s[0][p-1]-2
        b[0][p]="←"
    for p in range(1,len(v)+1):
        s[p][0]=s[p-1][0]-2
        b[p][0]="↑"
    table(s,b,v,w,mat,mis,ind)
    return s,b

def llcs(v,w,mat,mis,ind):
    s=[[0]*(len(w)+1) for i in range(len(v)+1)]
    b=[['']*(len(w)+1) for i in range(len(v)+1)]
    for p in range(1,len(w)+1):
        b[0][p]="←"
    for p in range(1,len(v)+1):
        b[p][0]="↑"
    table(s,b,v,w,mat,mis,ind)
    return s,b

def table(s,b,v,w,mat,mis,ind):
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):           
            score=0
            if v[i-1]==w[j-1]:
                score=s[i-1][j-1]+mat
            else:
                score=s[i-1][j-1]+mis
            vind=s[i-1][j]+ind
            wind=s[i][j-1]+ind
            s[i][j]=max(score,vind,wind)
    
            sbuf1=s[i-1][j-1]+mat
            sbuf2=s[i-1][j-1]+mis
            
            if s[i][j]==vind:
                b[i][j]=b[i][j]+'↑'
            if s[i][j]==wind:
                b[i][j]=b[i][j]+'←'            
            if v[i-1]==w[j-1]:
                if s[i][j]==sbuf1 or s[i][j]==sbuf2:
                    b[i][j]=b[i][j]+'↖︎'
    return 

def printglcs(s,b,v,w):
    k1=[]*len(w)
    for p in range(1,len(w)+1):
        if s[len(v)][p]==max(s[len(v)]):        
            i=len(v)
            j=p
            align(b,v,s[len(v)][p],i,j,k1)
    return k1

def printllcs(s,b,v,w):
    p1=[]*len(v)*len(w)
    p2=[]*len(v)*len(w)
    p3=[]*len(v)*len(w)
    for pi in range(1,len(v)+1):
        for pj in range(1,len(w)+1):
            if s[pi][pj]==max(s[pi]):
                p1.append(max(s[pi]))
                p2.append(pi)
                p3.append(pj)
    k1=[]*len(p1)
    
    for p in range(0,len(p1)):
        if p1[p]==max(p1):        
            i=p2[p]
            j=p3[p]
            align(b,v,p1[p],i,j,k1)
    return k1

def align(b,v,p,i,j,k1):
    k=''
    k2=[[],[]]
    k2[0]=p
    while i > 0 and j > 0:
        if "↖︎" in b[i][j]:
            k=v[i-1]+k
            i-=1
            j-=1
        elif "↑" in b[i][j]:
            i-=1
        else:
            j-=1
    k2[1].append(k)
    k1.append(k2)
    return

X1="GCATGCTA"
Y1="GATTACAA"
X2="GACTAC"
Y2="CGTGAATCAT"
print(X1,Y1)
s1,t1=glcs(X1,Y1,5,-1,-2)
for i in range(0,len(X1)+1):
    print(s1[i])
for i in range(0,len(X1)+1):
    print(t1[i])
q1=printglcs(s1,t1,X1,Y1)
print(q1)
print(X2,Y2)
s2,t2=llcs(X2,Y2,5,-3,-4)
for i in range(0,len(X2)+1):
    print(s2[i])
for i in range(0,len(X2)+1):
    print(t2[i])
q2=printllcs(s2,t2,X2,Y2)
print(q2)