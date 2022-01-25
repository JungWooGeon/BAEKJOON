from queue import PriorityQueue

q = PriorityQueue()

q.put(1)
q.put(5)
q.put(2)
q.put(10)
q.put(-99)
q.put(7)
q.put(5)


for i in range(7):
    print(q.get(i))