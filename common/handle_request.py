import requests
import json

class ApiRequest(object):
#     """
#     请求方法
#     """
#     # 请求方法get
#     def get_method(self,url,data,header):
#
#         if header is not None:
#             res = requests.get(url,params=data,headers=header)
#         else:
#             res = requests.get(url,params=data)
#         return res.json()
#
#     # 请求方法post
    def post_method(self,url,data,headers):
        global res
        if header is not None:
            res = requests.post(url,json=data,headers=header)
        else:
            res = requests.post(url,json=data)
        if  str(res) == "<Response [200]>":
            return res.json()
        else:
            return res.text
#
#     # 请求方法put
#     def put_method(self,url,data,header):
#         if header is not None:
#             res = requests.put(url,json=data,headers=header)
#         else:
#             res = requests.delete(url, json=data)
#         return res.json()
#
#     # 请求方法delete
#     def delete_method(self, url, data, header):
#         if header is not None:
#             res = requests.delete(url, json=data, headers=header)
#         else:
#             res = requests.delete(url, json=data)
#         return res.json()
#
#     # 主方法
#     def run_method(self,method,url,data,header):
#         if method == 'get' or method == 'GET':
#             res = self.get_method(url,data,header)
#         elif method == 'post' or method =='POST':
#             res = self.post_method(url,data,header)
#         elif method == 'put' or method == 'PUT':
#             res = self.post_method(url,data,header)
#         elif method == 'delete' or method == 'DELETE':
#             res = self.post_method(url,data,header)
#         else:
#             res = "你的请求方式不正确！"
#         # return res
#         return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True,separators=(',', ':'))
#
if __name__ == '__main__':
    ar =ApiRequest()
    url="http://192.168.1.211:8088/auth-app/auth/login"
    header = {"Content-Type": "application/json"}
    data= {"code":"48248060","password":"w123456"}
    ll = ar.post_method(url=url,data=data,headers=header)
    # res=ar.run_method(method='post',url=url,data=data,header=header)
    # print(res)
    print(ll)


# class ApiRequest:
#     """
#     请求方法
#     """
#
#     def send_requests(self,method=None,url=None,data=None,headers=None,json=None,params=None,files=None):
#         res = requests.request(method=method,url=url,data=data,headers=headers,json=json,params=params,files=files)
#
#         return res
