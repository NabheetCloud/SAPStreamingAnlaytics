import psutil
import time
import requests
import json
import ast
# Get Authorization token
authorizationURL = 'http://hxehost:39045/1/authorization'
headersAuthorization = {
    "Authorization": "Basic <base64 username/password>"    
}
payloadAuthorization = [
{ "privilege":"write", "resourceType":"stream", "resource":"default/zram2/MACHINEDATA"}
]
responseAuthorization = requests.post(authorizationURL,data=json.dumps(payloadAuthorization), headers=headersAuthorization)
r = responseAuthorization
r1 = json.loads(json.dumps(r.text))
r2 = r1.split(':')
r3 = r2[1].split("}")

#Post Data
postDataURL = 'http://hxehost:39045/1/workspaces/default/projects/zram2/streams/MACHINEDATA'
headersPostData = {
"authorization":"SWS-Token \"sws-token\"=" + r3[0]	
}
#print(headersPostData)

count = 0
while count < 5:
	count += 1
	p = psutil.virtual_memory()
	print p.percent
	time.sleep(10)
	payloadPostData = [
	{"ESP_OPS":"i", "MACHINEID":"1A", "EVENT_TIME": "2018-05-14T04:45:36.123", "EVENT_NAME":"TEMP"
	, "EVENT_DESCRIPTION":"RAM Usage", "EVENT_VALUE":str(p.percent)}
    ]

	responsePost = requests.post(postDataURL,data=json.dumps(payloadPostData), headers=headersPostData) 
#	print(payloadPostData)
	print(responsePost)
	