from pwn import *

n = 1000
F = [0]*(n+1)
F[0] = 4
F[1] = 5

S = [0]*(n+1)
S[0] = 4

Ssum = [0]*(n+1)
Ssum[0] = 4

def fib(i):
	global F
	F[i] = F[i-1]+F[i-2]

def Sseq(i):
	global S
	S[i] = S[i-1]+F[i]

def Ssumseq(i):
	global Ssum
	Ssum[i] = Ssum[i-1] + S[i]

def get_ans(i):
	global Ssum
	return int(str(Ssum[i])[-10:])

#populate F
for i in range(2,n+1):
	fib(i)

#populate S
for i in range(1, n+1):
	Sseq(i)

#populate Ssum
for i in range(1,n+1):
	Ssumseq(i)


conn = remote("extended-fibonacci-sequence-2.hsc.tf", 1337)
a = conn.recvline().decode("utf-8")
print(a)


while(True):
	a = conn.recvline().decode("utf-8")
	print(a)
	a = conn.recvline().decode("utf-8")
	print(a)
	b = conn.recvline().decode("utf-8")
	print(b)
	ans = get_ans(int(b))
	print(ans)
	conn.send(str(ans)+"\n")
	a = conn.recvline().decode("utf-8")
	print(a)
	