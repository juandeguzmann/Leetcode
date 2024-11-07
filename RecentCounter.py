class RecentCounter:
    TIME_WINDOW = 3000

    def __init__(self):
        self.data = deque()

    def ping(self, t):
        self.data.append(t)

        # remove all calls older than TIME_WINDOW
        while self.data[0] < t - self.TIME_WINDOW:
            self.data.popleft()
        
        return len(self.data)

from collections import deque

data = deque()
def recentCounter(t):
    data.append(t)

    while data[0] < (t - 3000):
        data.popleft()
    
    print(len(data), data)

recentCounter(2)
recentCounter(100)
recentCounter(3001)
recentCounter(3003)

