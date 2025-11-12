class N:
    def __init__(s,k):s.k=k;s.l=s.r=None
def ins(r,k):
    if not r:return N(k)
    if k<r.k:r.l=ins(r.l,k)
    elif k>r.k:r.r=ins(r.r,k)
    return r
def sea(r,k):
    if not r or r.k==k:return r
    return sea(r.l,k) if k<r.k else sea(r.r,k)
def mini(r):
    while r.l:r=r.l
    return r
def dele(r,k):
    if not r:return r
    if k<r.k:r.l=dele(r.l,k)
    elif k>r.k:r.r=dele(r.r,k)
    else:
        if not r.l:return r.r
        if not r.r:return r.l
        t=mini(r.r);r.k=t.k;r.r=dele(r.r,t.k)
    return r
def ino(r):
    if r:ino(r.l);print(r.k,end=' ');ino(r.r)

r=None
for x in [50,30,70,20,40,60,80]:r=ins(r,x)
print("Inorder:");ino(r)
print("\nSearch 40:",'Found'if sea(r,40)else'Not Found')
r=dele(r,20);print("After delete 20:");ino(r)