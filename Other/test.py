from collections import Counter
s = 'asdfasdfasdfasdf'
for x,val in Counter(s).items():
    print(x,val,sep = " ")