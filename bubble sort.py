def arr(b):
    for i in range(0,len(b)-1):
        for j in range(0,len(b)-1):
            if b[j]< b[j+1]:
                continue
            else:
                b[j], b[j+1]=b[j+1], b[j]
    print(b)
n=[1,6,2,8,4,9]
arr(n)
