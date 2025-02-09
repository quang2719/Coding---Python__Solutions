def createCode(s):
    ch = [x for x in s]
    ch.sort()
    i = 0
    res = []
    while i < len(s):
        j = i
        while j < len(s) and ch[i] == ch[j]:
            j+=1
        res.append(ch[i])
        res.append(f'{j-i}')
        i = j
    return ''.join(res)
print(createCode('dd'))