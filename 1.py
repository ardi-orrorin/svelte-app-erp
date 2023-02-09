import json


with open(f'sql_info.json')as f:
    DBINFO = json.load(f)

print(DBINFO['origin'])
