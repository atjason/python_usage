import httpx

# Passing Parameters In URLs, Custom Headers
params = {'key1': 'value1', 'key2': 'value2'}
headers = {'user-agent': 'my-app/0.0.1'}
r = httpx.get('https://postman-echo.com/get', params=params, headers=headers)
r.url # 'https://postman-echo.com/get?key1=value1&key2=value2'

# Response
# r.text
# r.json()
# r.json()['headers']['user-agent'] # 'my-app/0.0.1'
# r.status_code # 200
# r.status_code == httpx.codes.ok

# POST
data = {'key1': 'value1', 'key2': 'value2'}
# headers = {'content-type': 'application/x-www-form-urlencoded'}
r = httpx.post('https://postman-echo.com/post', data=data) # No need to set 'content-type' in headers.
str(r.json()['json']) # "{'key1': 'value1', 'key2': 'value2'}"
r.json()['headers']['content-type'] # 'application/x-www-form-urlencoded'

r = httpx.post('https://postman-echo.com/post', json=data)
str(r.json()['json']) # "{'key1': 'value1', 'key2': 'value2'}"
r.json()['headers']['content-type'] # 'application/json'

# Cookies
cookies = {'key1': 'value1'}
r = httpx.get('https://postman-echo.com/cookies', cookies=cookies)
r.text # '{"cookies":{"key1":"value1"}}'
for k,v in r.cookies.items():
  print(k, v)

# Allow redirect
httpx.get('http://github.com/', follow_redirects=True)

# Timeout
try:
  httpx.get('https://postman-echo.com/cookies', timeout=0.001)
except httpx.exceptions.Timeout:
  print('Timeout')
