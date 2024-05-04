import requests as req

url = "https://littlecaesars.com/en-us/login/"

response = req.get(url, headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"})

response_req = response.request
response_content = response.content

print(response_req.url)
print(response_req.headers)
print(response_content.decode('utf-8'))
