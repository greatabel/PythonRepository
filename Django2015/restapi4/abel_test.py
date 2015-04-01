#记得自己更新密码，上传前我修改了
import requests
import pprint

response = requests.get('http://localhost:8000/api/')
print(response.status_code)
api = response.json()
pprint.pprint(api)

response = requests.get(api['sprints'])
print(response.status_code)

response = requests.get(api['sprints'], auth=('demo', 'abel'))
print(response.status_code)

import datetime
today = datetime.date.today()
two_weeks = datetime.timedelta(days=14)
data = {'name': 'Current Sprint', 'end': today + two_weeks}
response = requests.post(api['sprints'], data=data, auth=('demo', 'abel'))

print(response.status_code)
sprint = response.json()
pprint.pprint(sprint)
