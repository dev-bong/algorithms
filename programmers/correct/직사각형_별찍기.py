a, b = map(int, input().strip().split(" "))

for i in range(b):
    tmp = ""
    for j in range(a):
        tmp += "*"
    print(tmp)