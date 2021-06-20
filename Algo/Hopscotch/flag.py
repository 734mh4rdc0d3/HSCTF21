from pwn import *

n = 1000
F = [0]*(n+1)
F[1] = 1
F[2] = 2


def fib(i):
	global F
	F[i] = F[i-1]+F[i-2]

#populate F
for i in range(3,n+1):
	fib(i)


conn = remote("hopscotch.hsc.tf", 1337)
a = conn.recvline().decode("utf-8")
print(a)
b = conn.recvline().decode("utf-8")
print(b)

ans = F[int(b)]%10000
print(ans)

conn.send(str(ans)+"\n")

while(True):
	b = conn.recvline().decode("utf-8")[2:]
	print(b)

	ans = F[int(b)]%10000	
	print(ans)

	conn.send(str(ans)+"\n")