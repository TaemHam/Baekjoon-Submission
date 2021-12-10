a, b = (input() for _ in range(2))
c = list(map(int,b[::-1]))
a, b = int(a), int(b)
for i in range(len(c)):
    print(a*c[i])
print(a*b)