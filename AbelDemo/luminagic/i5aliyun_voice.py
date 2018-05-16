import hashlib
import hmac
import base64
import datetime
import ssl
import requests


class HttpProxy:
    """
    Http工具类，封装了鉴权
    """

    def __init__(self, ak_id, ak_secret, model):
        self.__ak_id = ak_id
        self.__ak_secret = ak_secret
        # 必填
        self.__version = "2.0"
        self.__model = model
        # 音频文件长度
        self.f_len = None

    def __current_gmt_time(self):
        return datetime.datetime.strftime(datetime.datetime.utcnow(), "%a, %d %b %Y %H:%M:%S GMT")

    def __md5_base64(self, body):
        hash = hashlib.md5()
        hash.update(body)
        return base64.b64encode(hash.digest()).decode('utf-8')

    def __sha1_base64(self, str_to_sign, secret):
        hmacsha1 = hmac.new(secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha1)
        return base64.b64encode(hmacsha1.digest()).decode('utf-8')

    def send_request(self, body, audio_format, sample_rate, url):
        gmtnow = self.__current_gmt_time()
        temp_body = self.__md5_base64(body)
        body_md5 = self.__md5_base64(temp_body.encode('utf8'))
        content_type = "audio/" + audio_format + ";samplerate=" + str(sample_rate)
        str_to_sign = "POST" + "\n" + "application/json" + "\n" + body_md5 + "\n" + content_type + "\n" + gmtnow
        signature = self.__sha1_base64(str_to_sign, self.__ak_secret)
        auth_header = "Dataplus " + self.__ak_id + ":" + signature
        ssl._create_default_https_context = ssl._create_unverified_context
        url = url + "model=" + self.__model + "&" + "version=" + self.__version
        headers = {
            "Accept": "application/json",
            "Content-Type": content_type,
            "Date": gmtnow,
            "Authorization": auth_header,
            "Content-Length": str(self.f_len)
        }
        r = requests.post(url, data=body, headers=headers)
        return r.json().get("result")

    def read_file(self, file_path):
        file = open(file_path, 'rb')
        sound_wav_rb = file.read()
        file.close()
        # 这里要转换成字节数组
        temp_byte = bytearray(sound_wav_rb)
        print(temp_byte)
        return temp_byte


if __name__ == '__main__':
    # chat可以根据自己的情景修改，这里阿里云文档已经标明
    http_proxy = HttpProxy("id", "key", "chat")
    # 读取文档 
    sound_wav_rb = http_proxy.read_file("/Users/wanchang/Desktop/mount.wav")
    # 这里的参数详见文档
    response = http_proxy.send_request(sound_wav_rb, "wav", 16000, "https://nlsapi.aliyun.com/recognize?")
    print(response)
