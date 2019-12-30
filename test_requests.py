import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# print(f"The status code is {res.status_code}")
#
#
# print("The old statuscode is %s" %(res.status_code))

print(res.text[0:500])


#Will raise an exception if the request is not a valid one
res.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

