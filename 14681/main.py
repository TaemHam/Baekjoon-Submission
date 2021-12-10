x,y = [int(input()) for _ in range(2)]
z = [1,4,2,3]
z = z[0:2] if x > 0 else z[2:4]
z = z[0] if y > 0 else z[1]
print(z)