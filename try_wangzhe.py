import requests
from lxml import etree
import time,random


headers = {
        "User-Agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; OPPO R11 Build/NMF26X)"
}

def down_firstweb(url):
    try:
        response = requests.get(url, headers=headers, verify=False)
        conts = response.json()['news_list']
        for temp in conts:
            title = temp['title']
            keyword_name = temp['keyword_name']
            release_time = temp['cover'].split("_")[0].split("/")[-1]
            img_url = temp['thumb_img'][0]
            print("标题：", title)
            print("关键字：", keyword_name)
            print("发表时间：", release_time)
            print("标题图片链接：",img_url)

            print("*" * 50, "华丽的分隔符", "*" * 50)
    except Exception as e:
        print(e)

def down_web(index):
    try:
        while True:
            index +=1
            url = f"http://gamehelper.gm825.com/wzry/news/list?pn={index}&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=35E4D200F695F9A9F643683BD90D25AB&ovr=4.4.2&device=OPPO_OPPO+R11&net_type=1&client_id=ndOlwsXBMtzt1FOpvdGrWw%3D%3D&info_ms=RHM7aDPyT7iPm%2Bi8uCghyA%3D%3D&info_ma=MoP9crytiQ6PPFXluYOC8%2Bpzhi%2FBhQas1KZ3za%2F6YOI%3D&mno=0&info_la=V73h90kyeGHUCE%2Fi3hqqqA%3D%3D&info_ci=V73h90kyeGHUCE%2Fi3hqqqA%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=MoP9crytiQ6PPFXluYOC8%2Bpzhi%2FBhQas1KZ3za%2F6YOI%3D&os_level=19&os_id=4ccc6adde82d3445&resolution=720_1280&dpi=240&client_ip=192.168.11.142&pdunid=adde82d28374ccc6"
            response = requests.get(url, headers=headers, verify=False)
            conts = response.json()['list']
            for temp in conts:
                title = temp['title']
                keyword_name = temp['keyword_name']
                release_time = temp['cover'].split("_")[0].split("/")[-1]
                img_url = temp['thumb_img'][0]
                print("标题：", title)
                print("关键字：", keyword_name)
                print("发表时间：", release_time)
                print("标题图片链接：",img_url)

                print("*" * 50, "华丽的分隔符", "*" * 50)
                down_web(index)
    except Exception as e:
        print("已经没有数据了.....")


if __name__ == '__main__':
    url =  "http://gamehelper.gm825.com/wzry/hot/information?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=35E4D200F695F9A9F643683BD90D25AB&ovr=4.4.2&device=OPPO_OPPO+R11&net_type=1&client_id=ndOlwsXBMtzt1FOpvdGrWw%3D%3D&info_ms=RHM7aDPyT7iPm%2Bi8uCghyA%3D%3D&info_ma=MoP9crytiQ6PPFXluYOC8%2Bpzhi%2FBhQas1KZ3za%2F6YOI%3D&mno=0&info_la=V73h90kyeGHUCE%2Fi3hqqqA%3D%3D&info_ci=V73h90kyeGHUCE%2Fi3hqqqA%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=MoP9crytiQ6PPFXluYOC8%2Bpzhi%2FBhQas1KZ3za%2F6YOI%3D&os_level=19&os_id=4ccc6adde82d3445&resolution=720_1280&dpi=240&client_ip=192.168.11.142&pdunid=adde82d28374ccc6"
    down_firstweb(url)
    down_web(1)