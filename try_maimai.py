import requests

import time,random


headers = {
        "User-Agent": "{OPPO OPPO R11} [Android 4.4.2/19]/MaiMai 5.0.16(10018)"
}

def down_firstweb(url):
    try:
        response = requests.get(url, headers=headers, verify=False)
        conts = response.json()['feeds']

        for temp in conts:
            try:
                cont = temp['style1']['copy_text'].replace("\n","")
                author = temp['style1']['header']['title'].split("33>")[-1].split("</")[0]
                position = temp['style1']['header']['desc'].split("AA>")[-1].split("</")[0]
                img_urls = temp['style1']['imgs']
                url = []
                for img in img_urls:
                    img_url = img['turl']
                    url.append(img_url)
            except:
                continue

            print("内容简介：",cont)
            print("楼主：", author)
            print("公司及职位描述：", position)
            print("标题图片链接：",url)

            print("*" * 50, "华丽的分隔符", "*" * 50)
    except Exception as e:
        print(e)

def down_web(index):
    try:
        url = f"https://open.taou.com/maimai/feed/v5/nd1feed?u=228810530&access_token=1.dd3171637d0c61a9826a11a5e0209d91&version=5.0.16&ver_code=android_10018&channel=Web&vc=Android%204.4.2%2F19&push_permit=1&net=wifi&open=icon&appid=3&device=OPPO%20OPPO%20R11&imei=866174010276109&udid=86dc0f65-ccda-4c33-af32-290fcff9397d&is_push_open=1&isEmulator=0&density=1.5&launch_uuid=ec2cdf04-8bdd-4951-bffa-e279fa7bce80&session_uuid=c3adec88-0854-48db-8b9e-0f28c5ed283e&from_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.fragment.ExpandListFragment%26uuid%3D3e38cac6-ceea-4b9b-9f0e-57c8fd3e29dd%26url%3Dtaoumaimai%253A%252F%252Fhome%253Fhosttype%253D101&src_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.SplashActivity%26uuid%3Dde51aa37-eb20-4fc7-826a-2b8af7432b41&to_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.fragment.ExpandListFragment%26uuid%3D3e38cac6-ceea-4b9b-9f0e-57c8fd3e29dd%26url%3Dtaoumaimai%253A%252F%252Fhome%253Fhosttype%253D101&last_launch_time=1568950347867&action=load_more&thumb_size=404&page_tab=explore_list&page={index}&pfmj_commend_cnt=0"
        response = requests.get(url, headers=headers, verify=False)
        conts = response.json()['feeds']
        for temp in conts:
            try:
                cont = temp['style1']['copy_text'].replace("\n","")
                author = temp['style1']['header']['title'].split("33>")[-1].split("</")[0]
                position = temp['style1']['header']['desc'].split("AA>")[-1].split("</")[0]
                img_urls = temp['style1']['imgs']
                url = []
                for img in img_urls:
                    img_url = img['turl']
                    url.append(img_url)
            except:
                continue
            print("内容简介：",cont)
            print("楼主：", author)
            print("公司及职位描述：", position)
            print("标题图片链接：",url)

            print("*" * 50, "华丽的分隔符", "*" * 50)
        index += 1
        down_web(index)
        time.sleep(random.random*3)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = "https://open.taou.com/maimai/feed/v5/nd1feed?u=228810530&access_token=1.dd3171637d0c61a9826a11a5e0209d91&version=5.0.16&ver_code=android_10018&channel=Web&vc=Android%204.4.2%2F19&push_permit=1&net=wifi&open=icon&appid=3&device=OPPO%20OPPO%20R11&imei=866174010276109&udid=86dc0f65-ccda-4c33-af32-290fcff9397d&is_push_open=1&isEmulator=0&density=1.5&launch_uuid=1715b6cd-1d16-4096-a919-fa3e0f14f339&session_uuid=669325d0-9041-4e67-9bf5-6bc2860d0b22&from_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.SplashActivity%26uuid%3D15f6e82e-6a20-446e-973a-e4cfb07ed544&src_page=&to_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.SplashActivity%26uuid%3D15f6e82e-6a20-446e-973a-e4cfb07ed544&last_launch_time=1568950353569&action=out_date&thumb_size=404&page_tab=explore_list&page=0&pfmj_commend_cnt=0"
    down_firstweb(url)
    down_web(1)




