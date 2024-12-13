nums = [10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42]
s_num = [(x,i) for i,x in enumerate(nums)]
s_num.sort(key = lambda x : x[0])
print(s_num)