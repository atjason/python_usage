import heapq

# Find N largest and smallest items from a list.

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(3, nums) # [42, 37, 23]
heapq.nsmallest(3, nums) # [-4, 1, 2]

portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
  {'name': 'AAPL', 'shares': 50, 'price': 543.22},
  {'name': 'FB', 'shares': 200, 'price': 21.09},
  {'name': 'HPQ', 'shares': 35, 'price': 31.75},
  {'name': 'YHOO', 'shares': 45, 'price': 16.35},
  {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]
heapq.nlargest(2, portfolio, key=lambda stock: stock['shares'] * stock['price'])

# PriorityQueue

class PriorityQueue:
  def __init__(self):
    self._queue = []
    self._index = 0

  def push(self, item, priority):
    queue_item = (priority, self._index, item)
    heapq.heappush(self._queue, queue_item)
  
  def pop(self):
    queue_item = heapq.heappop(self._queue)
    return queue_item[-1]

pq = PriorityQueue()
pq.push('B', 2)
pq.push('C', 3)
pq.push('A', 1)

pq.pop() # 'A'
