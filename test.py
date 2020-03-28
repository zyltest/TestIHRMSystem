# a = {
#     "casename": "登录成功",
#     "login_body": {
#         "mobile": "13800000002",
#         "password": "123456"
#     },
#     "http_code": 200,
#     "success": True,
#     "code": 10000,
#     "message": "操作成功"
# }
# print(a.values())
# print(tuple(a.values()))
# print(a.items())
# print(a.keys())

b = {
    "add_emp": {
        "username": "葫芦娃xxsupe007",
        "mobile": "14790123809",
        "http_code": 200,
        "success": True,
        "code": 10000,
        "message": "操作成功"
    }
}

result = b.get("add_emp").values()
print(result)
