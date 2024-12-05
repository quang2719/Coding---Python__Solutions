arr = [1,2,3,4,5]
l = 0
while l < len(arr):
    if arr[l] %2 == 0:
        arr.insert(l,2)
        l+=2
    else: l+=1

print(arr)