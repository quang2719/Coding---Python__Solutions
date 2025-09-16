s = '1122211'
def maxDifference( s):
    count = [[0] for _ in range(5)]
    for x in s:
        for i in range(5):
            count[i].append(count[i][-1])
        count[int(x)][-1] = count[int(x)][-1] + 1
    return count
count = maxDifference(s)
for a in count:
    for b in a: print(b,end = ' ')
    print()