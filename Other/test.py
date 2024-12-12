from queue import PriorityQueue
def pickGifts(gifts, k):
    qp = PriorityQueue()
    for x in gifts:
        qp.put(-x)
    while k > 0:
        max_val = -qp.get()
        behind = max_val // (max_val**0.5)
        qp.put(-behind)
        k-=1
    res = 0
    while not qp.empty():
        res += -qp.get()
    return res
print(pickGifts([25,64,9,4,100],4))