from pwn import *

def solve(s):

	additions  = s.split("m")
	multiplications = []
	for term in additions:
		if "a" in term:
			add = term.split("a")
			add_val = 0
			for val in add:
				add_val = add_val + int(val)
			multiplications.append(str(add_val))
		else:
			multiplications.append(term)

	ans = 1
	for term in multiplications:
		ans*= int(term)

	return ans%(pow(2,32)-1)

conn = remote("not-really-math.hsc.tf", 1337)
a = conn.recvline().decode("utf-8")
print(a)
b = conn.recvline().decode("utf-8")
print(b)

ans = solve(b)
print(ans)

conn.send(str(ans)+"\n")

while(True):
	b = conn.recvline().decode("utf-8")[2:]
	print(b)

	ans = solve(b)
	print(ans)

	conn.send(str(ans)+"\n")