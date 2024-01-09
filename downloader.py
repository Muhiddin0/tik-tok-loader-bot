import requests
from bs4 import BeautifulSoup


class Loader:

    soup = None

    def single():
        
        title = Loader.soup.find_all('h3')[-1].text
        img = Loader.soup.find('img', {
            'src':True
        })['src']
        links = Loader.soup.find_all('a', {
            'onclick':'showAd()',
            'href':True,
        })
        return {
            'status':True,
            'type':'single',
            'title':title,
            'img':img,
            'links':links[1:]
        }
    
    def albom():
        image_links = Loader.soup.find_all('img', {
            'alt':True,
            'src':True
        })

        audio = Loader.soup.find('a', {
            'class':'tik-button-dl button dl-success',
            'onclick':'showAd()',
            'href':True
        })['href']

        return {
            'status':True,
            'type':'albom',
            'links':image_links,
            'audio':audio
        }
    
    def loading(url):
        cookies = {
            '__gpi': 'UID=00000caa5326827c:T=1698465380:RT=1698465380:S=ALNI_MbiDAORbdJwNS710qSoipx1F89JjA',
            '__gsas': 'ID=9535a63e2f10e3b4:T=1698465383:RT=1698465383:S=ALNI_MZUSK-Vt-yrA4iM6MLnuI0x64c3zQ',
            '.AspNetCore.Antiforgery.pqfZ5BU9LIk': 'CfDJ8M4Wma-fF3NGnoPyczPT0b9JyHHh2utXTg6LAg0vY20VPwn5v4ROhSmDC94mf9Vi0xRZEQ8PxCD2ufbmD7-Ya-XA005XjTUEk_GIO1b98AcFI3xQ2EM3PvWg80dRSWydQcOpxq4Gw9mDIJojANzuMkc',
            '__gads': 'ID=c1eac6890b0c8dd3-22427bf217e3003a:T=1698465380:RT=1698465424:S=ALNI_MbtH1WTEv6INNavZk9Mn4UlqWWwiQ',
        }

        headers = {
            'authority': 'tikvideo.app',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uz;q=0.6',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '__gpi=UID=00000caa5326827c:T=1698465380:RT=1698465380:S=ALNI_MbiDAORbdJwNS710qSoipx1F89JjA; __gsas=ID=9535a63e2f10e3b4:T=1698465383:RT=1698465383:S=ALNI_MZUSK-Vt-yrA4iM6MLnuI0x64c3zQ; .AspNetCore.Antiforgery.pqfZ5BU9LIk=CfDJ8M4Wma-fF3NGnoPyczPT0b9JyHHh2utXTg6LAg0vY20VPwn5v4ROhSmDC94mf9Vi0xRZEQ8PxCD2ufbmD7-Ya-XA005XjTUEk_GIO1b98AcFI3xQ2EM3PvWg80dRSWydQcOpxq4Gw9mDIJojANzuMkc; __gads=ID=c1eac6890b0c8dd3-22427bf217e3003a:T=1698465380:RT=1698465424:S=ALNI_MbtH1WTEv6INNavZk9Mn4UlqWWwiQ',
            'origin': 'https://tikvideo.app',
            'pragma': 'no-cache',
            'referer': 'https://tikvideo.app/en',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            '__RequestVerificationToken': 'CfDJ8M4Wma-fF3NGnoPyczPT0b_b2glgGtsb2HWuKbHFIFW43P1lhg2Jzk64h2dJjD5Kigd7ev86JmR36g7Hv7KOwrC3Bv_5qeawEVkyB1KkdcjVmbRiR39C0tAvCp7XHYdVIeoiz1ZwwItNK5wqDhTcUbY',
            'q': url,
        }

        response = requests.post('https://tikvideo.app/api/ajaxSearch', cookies=cookies, headers=headers, data=data).json()

        if 'statusCode' in response:
            return {
                'status':False,
            }
        
        soup = BeautifulSoup(response['data'], 'lxml')
        Loader.soup = soup
        
        is_albom = soup.find('div', {
            'class':'photo-list'
        })

        if is_albom:
            return Loader.albom()
        
        return Loader.single()



# print(
#     Loader.loading('https://vt.tiktok.com/ZSNBR9ats/') # storys
# )
# Loader.loading('https://vt.tiktok.com/ZSdsNBR9atcsds/') # storys baddd -> {'status': 'ok', 'statusCode': 404, 'msg': 'Video not found. Maybe the video is private or blocked.'}
# print(
#     Loader.loading('https://www.tiktok.com/@barsha_bhatta/video/7262692425204780306?is_from_webapp=1&sender_device=pc')
#) # post

# print(
#     Loader.loading('https://www.tiktok.com/@4kwallpaperssss/video/7199645742162627845') #post_albom
# ) https://www.tiktok.com/@4kwallpaperssss/video/7281453730858274053