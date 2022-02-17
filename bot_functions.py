import json
from stream_urls import StreamUrls
s = StreamUrls()

class Functions:

    def get_streamlink(self, url):
        if "buzzcast" in url:
            return self.get_faceurl(url)
        if "cam4" in url:
            return self.get_cam4url(url)
        if "chaturbate" in url: 
            return self.get_chatururl(url)
        if "tiktok" in url:
            return self.get_tiktok(url)

    def get_cam4url(self, url):
        if url.endswith('/'):
            url = url[:-1]
        username = url.split('/')[-1]
        response = s.cam4_streamInfo(username)
        if response:
            cdnUrl = response['cdnURL']
            can = response['canUseCDN']
            return f"{cdnUrl}"
        return "Sorry, something went wrong :("
    
    def get_faceurl(self, url):
        response = s.facecast_request(url)
        if response:
            return response['result']['live']['hlsUrl']
        return "Sorry, something went wrong :("

    def get_chatururl(self, url):
        if url.endswith('/'):
            url = url[:-1]
        username = url.split('/')[-1]
        response = s.chaturbate_request(username)
        if response:
            url = response['url']
            return url
        return "Sorry, something went wrong :("

    def get_tiktok(seld, url):
        response = s.tiktok_request(url)
        if response:
            return response['/@:uniqueId/live']['liveData']['LiveUrl']
        return "Sorry, something went wrong :("