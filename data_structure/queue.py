from collections import deque

q = deque(maxlen = 3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q # deque([2, 3, 4])

q.appendleft(1)
q # deque([1, 2, 3])

q.pop() # 3
q.popleft() # 1
