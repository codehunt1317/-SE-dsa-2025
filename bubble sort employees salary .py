s=[47000.75,29000.00,60000.25,54000.60,51000.10,45000.45,61000.90]

# Selection Sort
a=s[:]
for i in range(len(a)):
    m=i
    for j in range(i+1,len(a)):
        if a[j]<a[m]: m=j
    a[i],a[m]=a[m],a[i]
print("Selection Sort:",a)
print("Top 5:",a[-5:][::-1])

# Bubble Sort
b=s[:]
for i in range(len(b)-1):
    for j in range(len(b)-i-1):
        if b[j]>b[j+1]: b[j],b[j+1]=b[j+1],b[j]
print("Bubble Sort:",b)
print("Top 5:",b[-5:][::-1])

# Time: O(n²) | Space: O(1)