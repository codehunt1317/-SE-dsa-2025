# Hash Table with Chaining
size = 10
ht = [[] for _ in range(size)]

def h(k): return k % size

def insert(k,v): ht[h(k)].append((k,v))

def search(k):
    for x,y in ht[h(k)]:
        if x==k: return y
    return "Not Found"

def delete(k):
    b=ht[h(k)]
    for i,(x,_) in enumerate(b):
        if x==k: b.pop(i); return "Deleted"
    return "Not Found"

# --- Demo ---
insert(11,"A"); insert(21,"B"); insert(5,"C")
print("Table:",ht)
print("Search 21:",search(21))
print(delete(11))
print("After delete:",ht)

# Time: O(1) avg | Space: O(n)