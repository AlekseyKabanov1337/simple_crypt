import random

a=random.randint(100,5000)
b=random.randint(100,5000)
#Создаём список простых числе в заданном диапозоне
prost=[]
prost.append(2)
for j in range(3,50):
	c=0
	for i in range(2,j):
		if j%i==0:
			c+=1
	if c==0:
		prost.append(j)			
print(prost)
#Выбираем случайное простое число из задонного списка случайных чисел
p=prost[random.randint(1,len(prost))]
print('our prime number: ',p)

def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
def primitive_root(p):
    required_set = set(num for num in range (1, p) if gcd(num, p) == 1)
    for g in range(1, p):
        actual_set = set(pow(g, powers) % p for powers in range (1, p))
        if required_set == actual_set:
            return g
g=primitive_root(p)
print('our primitive root: ', g)

A=g**a
B=g**b
K1=B**a
K2=A**b
if K1==K2:
	print('K1 = K2 = OK')
k1=open('keyA.txt','w')
k1.write(str(A))
k1.close
k2=open('keyB.txt','w')
k2.write(str(B))
k2.close
