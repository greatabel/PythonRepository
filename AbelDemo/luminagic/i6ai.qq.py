from os import environ
import hashlib
import urllib.parse

import time
import wave
import random
import base64
import threading

import requests
import json

ai_qq_appid = environ.get('ai_qq_appid', '')
ai_qq_appkey = environ.get('ai_qq_appkey', '')
print(ai_qq_appid, ai_qq_appkey)

def http_post(api_url, args):
    resp = requests.post(url=api_url, data=args)
    resp = json.loads(resp.text)
    return resp

def md5(string):
    string = string.encode('utf-8')
    md = hashlib.md5()
    # print(type(string),'#'*10)
    md.update(string)
    md5 = md.hexdigest().upper()
    return md5


def urlencode(args):
    tuples = [(k, args[k]) for k in sorted(args.keys()) if args[k]]
    query_str = urllib.parse.urlencode(tuples)
    return query_str

def signify(args, app_key):
    query_str = urlencode(args)
    query_str = query_str + '&app_key=' + app_key
    signiture = md5(query_str)
    return signiture

class BaseASR(object):

    ext2idx = {'pcm': '1', 'wav': '2', 'amr': '3', 'slk': '4'}

    def __init__(self, api_url, app_id, app_key):
        self.api_url = api_url
        self.app_id = app_id
        self.app_key = app_key

    def stt(self, audio_file, ext='wav', rate=16000):
        raise Exception("Not Implemented!")


class BasicASR(BaseASR):
    """ Online ASR from Tencent
    https://ai.qq.com/doc/aaiasr.shtml
    """

    def __init__(self, api_url='https://api.ai.qq.com/fcgi-bin/aai/aai_asr',
                 app_id=ai_qq_appid, app_key=ai_qq_appkey):
        super(BasicASR, self).__init__(api_url, app_id, app_key)

    def stt(self, audio_file, ext='wav', rate=16000):
        if ext == 'wav':
            wf = wave.open(audio_file)
            nf = wf.getnframes()
            audio_data = wf.readframes(nf)
            wf.close()
        else:
            raise Exception("Unsupport audio file format!")
        print(self.app_id, len(audio_data), type(audio_data))
        # audio_data = bytes('', encoding = 'utf-8')
        args = {
            'app_id': self.app_id,
            'time_stamp': str(int(time.time())),
            'nonce_str': '%.x' % random.randint(1048576, 104857600),
            'format': self.ext2idx[ext],
            'rate': str(rate),
            'speech': base64.b64encode(audio_data),
        }

        signiture = signify(args, self.app_key)
        print('#'*10)
        args['sign'] = signiture
        resp = http_post(self.api_url, args)
        print('resp=', resp)
        text = resp['data']['text'].encode('utf-8')

        return text

def test_basic_asr():
    audio_files = ['i6d.wav']
    asr_engine = BasicASR()
    for audio_file in audio_files:
        text = asr_engine.stt(audio_file, ext='wav')
        print(text)

if __name__ == "__main__":
    for i in range(0, 100):
        test_basic_asr()
        time.sleep(10)