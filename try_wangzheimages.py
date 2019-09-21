import requests
from lxml import etree
import time,random

def down_img(name,url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    with open(f'./images/{name}.jpg', 'wb') as file:
        file.write(response.content)
        print(f"{name}图片已经下载")

headers = {
        "User-Agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; OPPO R11 Build/NMF26X)"
}

url = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=35E4D200F695F9A9F643683BD90D25AB&ovr=4.4.2&device=OPPO_OPPO+R11&net_type=1&client_id=ndOlwsXBMtzt1FOpvdGrWw%3D%3D&info_ms=RHM7aDPyT7iPm%2Bi8uCghyA%3D%3D&info_ma=MoP9crytiQ6PPFXluYOC8%2Bpzhi%2FBhQas1KZ3za%2F6YOI%3D&mno=0&info_la=V73h90kyeGHUCE%2Fi3hqqqA%3D%3D&info_ci=V73h90kyeGHUCE%2Fi3hqqqA%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=MoP9crytiQ6PPFXluYOC8%2Bpzhi%2FBhQas1KZ3za%2F6YOI%3D&os_level=19&os_id=4ccc6adde82d3445&resolution=720_1280&dpi=240&client_ip=192.168.11.142&pdunid=adde82d28374ccc6"

response = requests.get(url, headers=headers, verify=False)
img_list = response.json()['list']

for img in img_list:
    img_url = img['cover']
    img_name = img['name']
    down_img(img_name,img_url)

