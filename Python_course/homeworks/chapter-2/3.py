
def summation(a):
    m = []
    m.append(a)
    maxi = max(m)
    for i in range (0, len(m)):
        m[i] /= maxi
    return sum(m)

m = []
a = input()
a = a.split(" ")
for i in range (0, len(a)):
    if (int(a[i]) < 0):
        a[i] = int(a[i]) * (-2)
        m.append(a[i])
    else:
        m.append(int(a[i]))

for i in range (0, len(m)):
    b = summation(m[i])


