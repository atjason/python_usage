import requests

# Passing Parameters In URLs, Custom Headers
params = {'key1': 'value1', 'key2': 'value2'}
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('https://postman-echo.com/get', params=params, headers=headers)
r.url # 'https://postman-echo.com/get?key1=value1&key2=value2'

# Response
# r.text
# r.json()
# r.json()['headers']['user-agent'] # 'my-app/0.0.1'
# r.status_code # 200
# r.status_code == requests.codes.ok

# POST
data = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/x-www-form-urlencoded'}
r = requests.post('https://postman-echo.com/post', headers=headers, data=data)
str(r.json()['json']) # "{'key1': 'value1', 'key2': 'value2'}"
r.json()['headers']['content-type'] # 'application/x-www-form-urlencoded'

r = requests.post('https://postman-echo.com/post', json=data)
str(r.json()['json']) # "{'key1': 'value1', 'key2': 'value2'}"
r.json()['headers']['content-type'] # 'application/json'

# Cookies
cookies = {'key1': 'value1'}
r = requests.get('https://postman-echo.com/cookies', cookies=cookies)
r.text # '{"cookies":{"key1":"value1"}}'
r.cookies.get_dict() # Cookies dict return from server.

# Timeout
try:
  requests.get('https://postman-echo.com/cookies', timeout=0.001)
except requests.exceptions.Timeout:
  print('Timeout')
