from collections import deque

players = input().split(" ")
turn = int(input())

q = deque(players)

counter = 0

while len(q) > 1:
    for _ in range(turn - 1):
        q.append(q.popleft())
    print(f"Removed {q.popleft()}")

print(f"Last is {q.popleft()}")
