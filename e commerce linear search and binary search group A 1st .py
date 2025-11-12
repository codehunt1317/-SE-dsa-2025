def linear_search(arr, t): return t in arr

def binary_search(arr, t):
    l, r = 0, len(arr)-1
    while l<=r:
        m=(l+r)//2
        if arr[m]==t:return True
        elif arr[m]<t:l=m+1
        else:r=m-1
    return False

ids = [123, 456, 789, 1011, 1213]
t = int(input("Enter ID: "))
print("Linear:", "Found" if linear_search(ids, t) else "Not Found")
print("Binary:", "Found" if binary_search(ids, t) else "Not Found")