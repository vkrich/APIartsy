import requests as rq
import json
import operator

client_id = "a1fde857781fea751551"
client_secret = "de9de656b5ccd0a9e007b321b6c74320"
url="https://api.artsy.net/api/artists/"

r = rq.post("https://api.artsy.net/api/tokens/xapp_token", data={'client_id': client_id, 'client_secret': client_secret})
x=json.loads(r.text)['token']

with open("dataset_24476_4.txt",'r') as f:
  data=f.readlines()
dic={}

for i in data:
  i=i[0:len(i)-1]
  r = rq.get(url+i, headers = {"X-Xapp-Token": x})
  r.encoding = 'utf-8'
  inf = json.loads(r.text)  
  dic[inf['sortable_name']]=inf['birthday']

#result = sorted(dic.items(), key=lambda x: (x['birthday'], x['name']))
result = dict(sorted(dic.items(), key=operator.itemgetter(1)))

with open('output.txt','w', encoding='utf-8') as out:
  for i in result:
   out.write(i +" "+str(dic[i])+'\n')