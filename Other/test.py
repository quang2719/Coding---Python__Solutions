s = "asakjhdfkas"

arr = [{}]
for i in range(len(s)):
    cur_dic = arr[i].copy()
    cur_x = s[i]
    cur_dic[cur_x] = cur_dic.get(cur_x,0) + 1
    arr.append(cur_dic)
print(arr)
print(len(arr))
def do():
    return ""
print(do)
    