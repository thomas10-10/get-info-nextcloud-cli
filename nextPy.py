import sys
import os
import pprint 
import json
import fire


import re
import requests
response = requests.get('http://next:password@nextcloud.mydomain2.com:8080/ocs/v2.php/apps/serverinfo/api/v1/info?format=json')
#response = requests.get('http://next:Zs2Km-4eFpE-qTFBd-pZfEL-erXxL@nextcloud.mydomain2.com:8080/ocs/v2.php/apps/serverinfo/api/v1/info?format=json')
result=response.json()

#nextcloud system version
raw=0
#nextcloud storage num_users

req=""
args=sys.argv
args.pop(0)

reqq="result['ocs']['data']"
for i in args :
    if i == "--raw":
        raw=1;
        pass
    matchObj = re.search("--", i)
    if not matchObj:
        req=req+"['"+str(i)+"']"
        reqq="result['ocs']['data']"+req

if raw == 1:
    print(eval(reqq))
else:
    print(json.dumps(eval(reqq),indent=4))
    
NEXTCLOUD_URL = os.environ['NEXTCLOUD_URL']
NEXTCLOUD_USER = os.environ.get('NEXTCLOUD_USER')
NEXTCLOUD_PASS = os.environ.get('NEXTCLOUD_PASS')

# True if you want to get response as JSON
# False if you want to get response as XML




