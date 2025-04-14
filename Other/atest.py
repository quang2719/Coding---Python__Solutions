arr = [1,2,1,12,2,2,3,4,4,3]
dic_list = {}
for i,x in enumerate(arr):
    if x in dic_list:
        dic_list[x].append(i)
    else:
        dic_list[x] = [i]
print(dic_list)