

import requests
import json

url = "https://api.scrape-it.cloud/scrape/google/locals"

headers = {
  'x-api-key': '1d2be82f940b4d53bd1d4716049a6a1f',
  'Content-Type': 'application/json'
}

with open("result.csv", "w") as f:
  f.write("position; title; phone; address; website; rating; reviews; type\n")

start = int(input("Start position: "))
pages = int(input("Number of pages: "))
with open("keywords.csv", "r+") as f:
  for keyword in f:
    for i in range(start, 20*pages, 20):
      temp = """{
        "country": "US",
        "domain": "com",
        "keyword": """+"\""+keyword.strip()+"\""+""",
        "ll": "@40.7455096,-74.0083012,14z",
        "start": """+str(i)+"""
      }
      """
      payload = json.loads(json.dumps(temp))
      response = requests.request("POST", url, headers=headers, data=payload)
      data = json.loads(response.text)
      try:
        for item in data["scrapingResult"]["locals"]:
          with open("result.csv", "a") as f:
            f.write(str(item["position"])+"; "+str(item["title"])+"; "+str(item["phone"])+"; "+str(item["address"])+"; "+str(item["website"])+"; "+str(item["rating"])+"; "+str(item["reviews"])+"; "+str(item["type"])+"\n")
      except Exception as e:
        print("There are no locals")



