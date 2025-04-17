def prime(a):
    q=[]
    for i in range (2,a):
        is_prime=True
        for j in range(2,i):
            if j%i==0:
                is_prime=False
                break
    if is_prime:
        q.append(i)
        return q
    
        







num=int(input("enter the number"))
b=prime(num)
print(b)
