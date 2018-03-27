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
#                b[i][j]=b[i][j]+'↖︎'
                if s[i][j]==sbuf1 or s[i][j]==sbuf2:
                    b[i][j]=b[i][j]+'↖︎'
#                elif s[i][j]==sbuf2:
 #                   b[i][j]=b[i][j]+'↖︎'
    return s,b

def llcs(v,w,mat,mis,ind):
    n=len(v)
    m=len(w)
    s=[[0]*(m+1) for i in range(n+1)]
#    d=[[0]*(m+1) for i in range(n+1)]
    b=[['']*(m+1) for i in range(n+1)]
    for p in range(1,m+1):
        b[0][p]="←"
    for p in range(1,n+1):
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
#                b[i][j]=b[i][j]+'↖︎'
                if s[i][j]==sbuf1 or s[i][j]==sbuf2:
                    b[i][j]=b[i][j]+'↖︎'
#                elif s[i][j]==sbuf2:
 #                   b[i][j]=b[i][j]+'↖︎'
    return s,b

def printglcs(s,b,v,w):
    for p in range(1,len(w)+1):
        k1=k2=''
        if s[len(v)][p]==max(s[len(v)]):        
            i=len(v)
            j=p
            while i > 0 and j > 0:
                if "↖︎" in b[i][j]:
                    k1=v[i-1]+k1
                    k2=w[i-1]+k2
                    i-=1
                    j-=1
            
                elif "↑" in b[i][j]:
                    k1=v[i-1]+k1
                    k2='_'+k2
                    i-=1

                else:
                    k1='_'+k1
                    k2=w[i-1]+k2
                    j-=1
            print(k1,k2)
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
    return

def printllcs(s,b,v,w):
    
    p1=[]*len(v)
    p2=[]*len(v)
    for p in range(1,len(v)+1):
        p1.append(max(s[p]))
        p2.append(s[p].index(max(s[p])))
    print(p1,p2)
    for p in range(0,len(p1)):
        k1=k2=''
        if p1[p]==max(p1):        
            i=p+1
            j=p2[p]
            while i > 0 and j > 0:
                if "↖︎" in b[i][j]:
                    k1=v[i-1]+k1
                    k2=w[i-1]+k2
                    i-=1
                    j-=1
            
                elif "↑" in b[i][j]:
                    k1=v[i-1]+k1
                    k2='_'+k2
                    i-=1
#                elif'←'in b[i][j]:
#                    k1='_'+k1
 #                   k2=w[i-1]+k2
  #                  j-=1
                else:
                    k1='_'+k1
                    k2=w[i-1]+k2
                    j-=1
            print(k1,k2)
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
printglcs(s1,t1,X1,Y1)
#print(w1,w2)
s2,t2=llcs(X2,Y2,5,-3,-4)
for i in range(0,len(X2)+1):
    print(s2[i])
for i in range(0,len(X2)+1):
    print(t2[i])
printllcs(s2,t2,X2,Y2)
#print(w3,w4)

#y=printllcs(u,X,b,len(X),len(Y))

