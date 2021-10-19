import requests
import time
import random
import hashlib
import json


class YouDao:
    def __init__(self, word):
        self.word = word
        self.formdata = None
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',
            'Referer': 'https://fanyi.youdao.com/',
            'cookie': '_ntes_nnid=b2bd3183b80a536b5e23a0517a0dbe09,1609301940731; OUTFOX_SEARCH_USER_ID_NCOO=96820041.49293956; OUTFOX_SEARCH_USER_ID="787599989@10.169.0.84"; JSESSIONID=aaa5u4ALZhnHhcfnoUsYx; ___rl__test__cookies=1634549585488'
        }

    def translation(self):
        self.config()
        response = requests.post(self.url, self.formdata, headers=self.headers)
        response.encoding = 'utf-8'
        try:
            data = json.loads(response.text)
            rdata = data['translateResult'][0][0]['tgt']
        except:
            rdata = 'error'
        return rdata

    def config(self):
        '''
        用于配置发送数据formdata
        '''

        ts = str(int(time.time() * 1000))
        i = ts + str(random.randint(0, 9))
        salt = i
        str_ = 'fanyideskweb' + self.word + i + "Y2FYu%TNSbMCxc3t2u^XT"
        md5 = hashlib.md5()
        md5.update(str_.encode('utf-8'))
        sign = md5.hexdigest()
        self.formdata = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': ts,
            'bv': '8f307b78e0cf5a0a41f77f2f8d464fe3',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }


if __name__ == '__main__':
    word = input('请输入要翻译的内容：')
    youdao = YouDao(word)
    print(youdao.translation())
