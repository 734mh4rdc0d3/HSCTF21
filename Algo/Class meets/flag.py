from pwn import *


conn = remote("class-meets.hsc.tf", 1337)

while True:
	
	a = conn.recvline().decode("utf-8")
	print(a)
	a = conn.recvline().decode("utf-8")
	print(a)
	a = conn.recvline().decode("utf-8")
	print(a)

	start = conn.recvline().decode("utf-8")
	print(start)

	end = conn.recvline().decode("utf-8")
	print(end)

	s1_sch = conn.recvline().decode("utf-8")
	print(s1_sch)

	s2_sch = conn.recvline().decode("utf-8")
	print(s2_sch)

	startM , startD = list(start.split(" "))#"M1" , "D5"
	endM, endD = list(end.split(" "))#"M2" , "D28"

	s1_ip , s1_v = list(s1_sch.split(" "))#"I5" , "V2"
	s1_str = s1_ip[0]*int(s1_ip[1:])+s1_v[0]*int(s1_v[1:])
	s1_index = int(s1_ip[1:])+int(s1_v[1:])
	s1_count = -1

	s2_ip , s2_v = list(s2_sch.split(" "))#"I8" , "V3"
	s2_str = s2_ip[0]*int(s2_ip[1:])+s2_v[0]*int(s2_v[1:])
	s2_index = int(s2_ip[1:])+int(s2_v[1:])
	s2_count = -1

	s1_cal = list("00000##")*51 + list("000") #360 days
	s2_cal = list("00000##")*51 + list("000") #360 days


	for i in range(0,360):
		if s1_cal[i] != "#":
			s1_count = (s1_count+1)%s1_index
			s1_cal[i] = s1_str[s1_count]

	for i in range(0,360):
		if s2_cal[i] != "#":
			s2_count = (s2_count+1)%s2_index
			s2_cal[i] = s2_str[s2_count]

	startindex = int(startM[1:])*30 + int(startD[1:])
	
	endindex = int(endM[1:])*30 + int(endD[1:])

	meetcount = 0 
	for i in range(startindex , endindex+1):
		if s1_cal[i] != "#" and s1_cal[i]==s2_cal[i]:
			meetcount+=1

	#print(s1_cal)
	#print(s2_cal)

	conn.send(str(meetcount)+"\n")
	print(meetcount)