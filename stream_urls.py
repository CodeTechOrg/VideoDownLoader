import requests
import json
from bs4 import BeautifulSoup


class StreamUrls:
    def tiktok_request(self, url):
        
        headers = { #m3u8 url is only present on mobile version of the website for some reason
            'User-Agent' : 'Mozilla/5.0 (Linux; Android 11; M2007J3SY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36'
        }

        response = requests.get(url, headers=headers, allow_redirects=True)
        soup = BeautifulSoup(response.text, 'html.parser')
        words = soup.find_all(text=lambda text: text and 'm3u8'.lower() in text)
        if len(words) > 0: 
            found = words[0]
        else:
            return None
        if "window.__INIT_PROPS__ = " in found:
            found = found.replace("window.__INIT_PROPS__ = ", '') #gambiarra total kkkkkkkkkkk
        return json.loads(found)

    def facecast_request(self, url):
        response = requests.get(url, allow_redirects=True)
        actualUrl = response.url
        liveId = actualUrl.split('/')[-1]
        data = {
            'liveId' : liveId
        }
        liveInfo = requests.get(url="https://sharing.buzzcast.info/share/third/live", params=data)
        if response.status_code == 200:
            return liveInfo.json()
        return None

    def chaturbate_request(self, username):
        url = "https://chaturbate.com/get_edge_hls_url_ajax/"
        headers = {"X-Requested-With": "XMLHttpRequest"}
        data = {"room_slug": username, "bandwidth": "high"}
        response = requests.post(url=url, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
        return None

    def cam4_streamInfo(self, username):
        url = f"https://www.cam4.com/rest/v1.0/profile/{username}/streamInfo"
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.json()
        return None

if __name__ == "__main__":
    s = StreamUrls()
    print(s.facecast_request("https://s.buzzcast.info/d/4zyN"))