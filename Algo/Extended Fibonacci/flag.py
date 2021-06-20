from pwn import *

n = 1000
F = [0]*(n+1)
F[1] = 1

S = [0]*(n+1)

Ssum = [0]*(n+1)

def fib(i):
	global F
	F[i] = F[i-1]+F[i-2]

def Sseq(i):
	global S
	S[i] = int(str(S[i-1])+str(F[i]))

def Ssumseq(i):
	global Ssum
	Ssum[i] = Ssum[i-1] + int(S[i])

def get_ans(i):
	global Ssum
	return int(str(Ssum[i])[-11:])

#populate F
for i in range(2,n+1):
	fib(i)

#populate S
for i in range(1, n+1):
	Sseq(i)

#populate Ssum
for i in range(1,n+1):
	Ssumseq(i)



conn = remote("extended-fibonacci-sequence.hsc.tf", 1337)
a = conn.recvline().decode("utf-8")
print(a)
b = conn.recvline().decode("utf-8")
print(b)

ans = get_ans(int(b))
print(ans)

conn.send(str(ans)+"\n")

while(True):
	b = conn.recvline().decode("utf-8")[2:]
	print(b)

	ans = get_ans(int(b))
	print(ans)

	conn.send(str(ans)+"\n")
	