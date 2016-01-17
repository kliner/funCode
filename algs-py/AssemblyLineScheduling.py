def carAssembly(a, t, e, x):
    n = len(a[0])
    T1, T2 = e[0]+a[0][0], e[1]+a[1][0]
    for i in xrange(1, n):
        T1, T2 = min(T1+a[0][i], T2+a[0][i]+t[1][i]), min(T1+a[1][i]+t[0][i], T2+a[1][i])
    return min(T1+x[0], T2+x[1])

   
a = [[4, 5, 3, 2], [2, 10, 1, 4]]
t = [[0, 7, 4, 5], [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7] 
print carAssembly(a,t,e,x)

