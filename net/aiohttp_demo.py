import asyncio
import aiohttp

# Make a Request

async def test_param(http_session):
  params = {'key1': 'value1', 'key2': 'value2'}
  headers = {'user-agent': 'my-app/0.0.1'}
  url = 'https://postman-echo.com/get'
  async with http_session.get(url, params=params, headers=headers) as resp:
    resp.status
    await resp.text()
    j = await resp.json()
    j['headers']['user-agent'] # 'my-app/0.0.1'

async def test_post1(http_session):
  data = {'key1': 'value1', 'key2': 'value2'}
  headers = {'content-type': 'application/x-www-form-urlencoded'}
  url = 'https://postman-echo.com/post'
  async with http_session.post(url, headers=headers, data=data) as resp:
    j = await resp.json()
    str(j['json']) # "{'key1': 'value1', 'key2': 'value2'}"
    j['headers']['content-type'] # 'application/x-www-form-urlencoded'

async def test_post2(http_session):
  data = {'key1': 'value1', 'key2': 'value2'}
  url = 'https://postman-echo.com/post'
  async with http_session.post(url, json=data) as resp:
    j = await resp.json()
    str(j['json']) # "{'key1': 'value1', 'key2': 'value2'}"
    j['headers']['content-type'] # 'application/json'

async def test_cookies(http_session):
  cookies = {'key1': 'value1'}
  url = 'https://postman-echo.com/cookies'
  async with http_session.get(url, cookies=cookies) as resp:
    j = await resp.json()
    j['cookies'] # '{"key1":"value1"}'

async def test_timeout(http_session):
  try:
    url = 'https://postman-echo.com/cookies'
    timeout = aiohttp.ClientTimeout(total=0.01)
    async with http_session.get(url, timeout=timeout):
      pass
  except asyncio.TimeoutError:
    print('Time out.')

async def main():
  http_session = aiohttp.ClientSession()

  await test_param(http_session)
  await test_post1(http_session)
  await test_post2(http_session)
  await test_cookies(http_session)
  await test_timeout(http_session)

  await http_session.close()

asyncio.run(main())
