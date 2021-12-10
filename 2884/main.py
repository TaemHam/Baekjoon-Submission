h,m = list(map(int,input().split()))
#m -= 45
#if m < 0:
#    m += 60
#    h -= 1
#    if h < 0:
#        h += 24
#print (h,m)
t=h*60+m-45
print(t,t//60)
print(t//60%24,t%60)