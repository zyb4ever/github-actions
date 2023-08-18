import requests
import random
import time
import os

url = "https://glados.rocks/api/user/checkin"

payload = "{\"token\":\"glados.one\"}"
headers = {
  'authority': 'glados.rocks',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-CN,zh;q=0.9',
  'authorization': '87591637160657701040902129014108-1440-2560',
  'content-type': 'application/json;charset=UTF-8',
  'cookie': '__stripe_mid=727c8c16-3cdd-4ce9-ba51-270559ec733a7da848; koa:sess=eyJ1c2VySWQiOjMyMTQ0LCJfZXhwaXJlIjoxNzE0MDQ1NTc4MDE2LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=74TElWubd2x9C5mxmv-_7fsD4LQ; _gid=GA1.2.765523720.1690860133; _ga=GA1.1.780350391.1673316798; _ga_CZFVKMNT9J=GS1.1.1690860133.15.1.1690860266.0.0.0; arp_scroll_position=112',
  'dnt': '1',
  'origin': 'https://glados.rocks',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

timeSecond = random.randint(1,59)
timeMin = random.randint(0,1)
# timeMin = 0
time.sleep(timeSecond+timeMin*60)

response = requests.request("POST", url, headers=headers, data=payload)


if (response.text.find("Checkin! Get 1 Day") != -1):
  print("success")
elif (response.text.find("Please Try Tomorrow") != -1):
  print("success")
else:
  print("fail")
