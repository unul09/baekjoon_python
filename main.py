# 3009

x = []
y = []
for _ in range(0, 3):
    px, py = map(int, input().split())
    x.append(px)
    y.append(py)

x.sort()
y.sort()

if x[0] == x[1]:
    px = x[2]
else:
    px = x[0]

if y[0] == y[1]:
    py = y[2]
else:
    py = y[0]

print(px, py)