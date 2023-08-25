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
  'authorization': '15530243933653734309100857125585-1080-1920',
  'content-type': 'application/json;charset=UTF-8',
  'cookie': '_ga=GA1.1.2054971322.1681306585; koa:sess=eyJ1c2VySWQiOjM5MDMzNCwiX2V4cGlyZSI6MTcxODI2MzUyMjY2NiwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=j90B0LBvwpVfgorQ4B51rXwBV_8; __stripe_mid=155e98c0-4823-465f-a85b-af375a17aea40afdc2; __stripe_sid=3cd7170a-c9cc-4564-b77a-b37b480e8ca13047fe; _ga_CZFVKMNT9J=GS1.1.1692954373.5.1.1692956137.0.0.0',
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
