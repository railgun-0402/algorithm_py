import json

def create_json(type_value, accountid_value, line_values):
    data = {
        "type": type_value,
        "account": {
            "accountid": accountid_value,
            "line": [{"id": line_id} for line_id in line_values]
        }
    }

    json_string = json.dumps(data, indent=2)
    return json_string

# 例: type=1, accountid=3314, line=[101, 102, 103]
# type_value = 1
# accountid_value = 3314
# line_values = [101, 102, 103]
#
# result_json = create_json(type_value, accountid_value, line_values)
# print(result_json)
#

# import json
# abc = '(105 OR 1=1)(" or ""=")(105; DROP TABLE Suppliers)'
# event = {"body": f'{{"dvcNo": "0001D","nodeIdList": [199],"reason": "{abc}"}}'}
# print(event["body"])
#
# data = json.loads(event["body"])

import json

abc = '(105 OR 1=1)(" or ""=")(105; DROP TABLE Suppliers)'
# JSON形式の文字列を構築する際にjson.dumps()を使用してエンコードする
event = {"body": json.dumps({"dvcNo": "0001D", "nodeIdList": [199], "reason": abc})}
print(event["body"])

# JSON形式の文字列をデコードする
data = json.loads(event["body"])
print(data)
