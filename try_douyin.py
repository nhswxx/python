import requests

import time,random

def down_video(name,url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    with open(f'G:/douyin/{name}.mp4', 'ab') as file:
        file.write(response.content)
        print(f"{name}视频已经下载")

headers = {
        "User-Agent": "okhttp/3.10.0.1" ,
        "Cookie": "Cookie: qh[360]=1; odin_tt=f939781ca25281fe220ee44a5c12919132c4a503f02be8c7662c7dcc9bb9ca5cf2c6144ec8274d951c75056e7f38bb99c910440d7111c711e7ed449e16a138ef; sid_guard=bb91744de38647c0c5efac28590c3079%7C1568983670%7C5184000%7CTue%2C+19-Nov-2019+12%3A47%3A50+GMT; uid_tt=db1098f9ebca622a9018e1a5932951f8; sid_tt=bb91744de38647c0c5efac28590c3079; sessionid=bb91744de38647c0c5efac28590c3079; install_id=86766150527; ttreq=1$44b4524133073f64df24395b4d83d466dd859291",
         "Accept-Encoding": "gzip",
        "X-Gorgon": "03b8b6bbc400593b009c07fc29d2818bb9be5c190e93b7eb6994",
        "X-Khronos": "1569035262",
        "x-tt-token": "00bb91744de38647c0c5efac28590c3079460ec0e50c8c04da01cdbd97034a84de454c1855c6a1325a8921dd08b36489ba57",
        "sdk-version": "1",
        "X-SS-REQ-TICKET": "1569035262848",
        "Connection": "Keep-Alive",
        "Host": "aweme-eagle.snssdk.com",
        "X-Pods": "",
}
url = "https://aweme-eagle.snssdk.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=-1&count=6&volume=0.7333333333333333&pull_type=2&need_relieve_aweme=0&filter_warn=0&req_from&is_cold_start=0&longitude=111.56895333918287&latitude=27.99775648309565&address_book_access=1&gps_access=1&ts=1569035262&js_sdk_version=&app_type=normal&openudid=4ccc6adde82d3445&version_name=6.5.0&device_type=OPPO%20R11&ssmix=a&iid=86766150527&os_api=19&mcc_mnc=46007&device_id=69555684288&resolution=720*1280&device_brand=OPPO%20&aid=1128&manifest_version_code=650&app_name=aweme&_rticket=1569035262854&os_version=4.4.2&device_platform=android&version_code=650&update_version_code=6502&ac=wifi&dpi=240&uuid=866174010276109&language=zh&channel=aweGW"
start_time = time.time()

while True:
    try:
        response = requests.get(url, headers=headers,verify=False)
        if response.json()['aweme_list']:
            video_url=response.json()['aweme_list']

            for each in video_url:
                #关键字段 描述、视频地址、作者昵称、发布时间
                desc=each['desc']
                videoUrl=each['video']['play_addr']['url_list'][0]
                author=each['author']['nickname']
                createTime=each['create_time']
                print('内容描述：',desc)
                print('视频地址：',videoUrl)
                print('作者昵称：',author)
                print('发布时间：',str(createTime))

                print("*" * 50, "华丽的分隔符", "*" * 50)

                down_video(desc, videoUrl)
                time.sleep(random.random())
            continue
        end_time = time.time()
        print("请求头已失效....请更换请求头 -.-")
        print("有效时间：",int((end_time - start_time) * 1000*1000/60),"分钟")
        break
    except:
        continue

