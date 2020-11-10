f=open("text.txt","r")
r=open("text3.txt","a")
k=0
for i in f:
    k=k+1
    p=str(k)
    r.write(p+"->> "+i+"\n\n")
