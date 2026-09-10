from collections import deque
fila = deque()
for i in range(1, 6):
     fila.append(i)
print(fila.popleft())
print(fila.popleft())