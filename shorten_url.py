# 단축 URL을 생성 동기, 비동기 처리

import requests
from bs4 import BeautifulSoup
import json
import asyncio
import time
import aiohttp
import sys


# -------------------- 서브루틴 --------------------

def han_gl(long_url):
    try:
        url = 'https://han.gl/shorten'
        response = requests.post(url, headers=headers, data={'url': long_url})
        r2 = json.loads(response.text)
        # print(r2['data']['shorturl'])
        shorten_url_result = r2['data']['shorturl']
    except Exception as e:
        print('Error1:', e)
        return None

    return shorten_url_result


def c11_kr(long_url):
    try:
        url = 'https://c11.kr/createurl.php'
        r1 = requests.get('https://c11.kr')
        soup = BeautifulSoup(r1.text, 'html.parser')
        hp = soup.find('input', id='hp')['value']
        response = requests.post(url, headers=headers, data={'urlr': long_url, 'hp': hp,})
        soup = BeautifulSoup(response.text, 'html.parser')
        shtn_url = soup.find('div', id='copyme')['data-clipboard-text']
        # print(shtn_url)
        shorten_url_result = shtn_url
    except Exception as e:
        print('Error2:', e)
        return None
    return shorten_url_result    


def shorturl_at(long_url):
    try:
        url = 'https://www.shorturl.at/shortener.php'
        response = requests.post(url, headers=headers, data={'u': long_url})
        soup = BeautifulSoup(response.text, 'html.parser')
        shtnUrl = soup.find('input', id='shortenurl')['value']
        shtn_url = 'https://' + shtnUrl
        # print(shtn_url)
        shorten_url_result = shtn_url
    except Exception as e:
        print('Error3:', e)
        return None
    return shorten_url_result    


def t2m_kr(long_url):
    try:
        url = 'http://t2m.kr/shorten'
        response = requests.post(url, headers=headers, data={'url': long_url})
        r2 = json.loads(response.text)
        # print(r2['short'])
        shorten_url_result = r2['short']
    except Exception as e:
        print('Error4:', e)
        return None
    return shorten_url_result


def vo_la(long_url):
    try:
        url = 'https://vo.la/shorten'
        response = requests.post(url, headers=headers, data={'url': long_url})
        r2 = json.loads(response.text)
        # print(r2['short'])
        shorten_url_result = r2['short']
    except Exception as e:
        print('Error5:', e)
        return None
    return shorten_url_result



# -------------------- 코루틴 --------------------

async def async_han_gl(long_url):
    async with aiohttp.ClientSession() as session:
        try:
            url = 'https://han.gl/shorten'
            async with session.post(url, data={'url': long_url}, headers=headers) as resp:
               r2 = await resp.json()
            # print(r2['data']['shorturl'])
            shorten_url_result = r2['data']['shorturl']
        except Exception as e:
            print('Error1:', e)
            return None

        return shorten_url_result


async def async_c11_kr(long_url):
    async with aiohttp.ClientSession() as session:
        try:
            url = 'https://c11.kr/createurl.php'
            async with session.get('https://c11.kr') as resp:
                r1 = await resp.text()
            soup = BeautifulSoup(r1, 'html.parser')
            hp = soup.find('input', id='hp')['value']
            async with session.post(url, headers=headers, data={'urlr': long_url, 'hp': hp,}) as resp2:
                response = await resp2.text()
            soup = BeautifulSoup(response, 'html.parser')
            shtn_url = soup.find('div', id='copyme')['data-clipboard-text']
            # print(shtn_url)
            shorten_url_result = shtn_url
        except Exception as e:
            print('Error2:', e)
            return None
        return shorten_url_result    


async def async_shorturl_at(long_url):
    async with aiohttp.ClientSession() as session:
        try:
            url = 'https://www.shorturl.at/shortener.php'
            async with session.post(url, headers=headers, data={'u': long_url}) as resp:
                response = await resp.text()
            soup = BeautifulSoup(response, 'html.parser')
            shtnUrl = soup.find('input', id='shortenurl')['value']
            shtn_url = 'https://' + shtnUrl
            # print(shtn_url)
            shorten_url_result = shtn_url
        except Exception as e:
            print('Error3:', e)
            return None
        return shorten_url_result    


async def async_t2m_kr(long_url):
    async with aiohttp.ClientSession() as session:
        try:
            url = 'http://t2m.kr/shorten'
            async with session.post(url, headers=headers, data={'url': long_url}) as resp:
                r2 = await resp.text()
            r2 = json.loads(r2)
            # print(r2['short'])
            shorten_url_result = r2['short']
        except Exception as e:
            print('Error4:', e)
            return None
        return shorten_url_result


async def async_vo_la(long_url):
    async with aiohttp.ClientSession() as session:
        try:
            url = 'https://vo.la/shorten'
            async with session.post(url, headers=headers, data={'url': long_url}) as resp:
                response = await resp.text()
            r2 = json.loads(response)
            # print(r2['short'])
            shorten_url_result = r2['short']
        except Exception as e:
            print('Error5:', e)
            return None
        return shorten_url_result



# -------------------- 코루틴 처리함수(run_in_executor 사용) --------------------

async def async_make_shortenUrl_1(func, url):
    loop = asyncio.get_event_loop()  # 현재의 이벤트 루프 반환
    res = await loop.run_in_executor(None, func, url)  # 동기 함수를 코루틴으로 실행하는 메소드
    print(f'\n단축URL : {res}')


async def async_main_1(long_url) : # 서브루틴을 이벤트 루프에 태우기
    await asyncio.gather(
        async_make_shortenUrl_1(han_gl, long_url),
        async_make_shortenUrl_1(c11_kr, long_url),
        async_make_shortenUrl_1(shorturl_at, long_url),
        async_make_shortenUrl_1(t2m_kr, long_url),
        # async_make_shortenUrl_1(vo_la, long_url),
    )



# -------------------- 서브루틴 처리함수 --------------------

def sync_make_shortenUrl(func, url):
    res = func(url)
    print(f'\n단축URL : {res}')

def sync_main(long_url):
    sync_make_shortenUrl(han_gl, long_url)
    sync_make_shortenUrl(c11_kr, long_url)
    sync_make_shortenUrl(shorturl_at, long_url)
    sync_make_shortenUrl(t2m_kr, long_url)
    # sync_make_shortenUrl(vo_la, long_url)


# -------------------- 코루틴 처리함수(코루틴만) --------------------

async def async_make_shortenUrl_2(func, url):
    res = await func(url)
    print(f'\n단축URL : {res}')


async def async_main_2(long_url) : # 서브루틴을 이벤트 루프에 태우기
    await asyncio.gather(
        async_make_shortenUrl_2(async_han_gl, long_url),
        async_make_shortenUrl_2(async_c11_kr, long_url),
        async_make_shortenUrl_2(async_shorturl_at, long_url),
        async_make_shortenUrl_2(async_t2m_kr, long_url),
        # async_make_shortenUrl_2(async_vo_la, long_url),
    )



# -------------------- 메인파트 --------------------

'''
python 3.8 이후부터 windows에서 async 한 개발을 하면 정상 동작을 하였음에도 불구하고 
다음과 같은 오류가 나타납니다.

RuntimeError: Event loop is closed

이러한 이슈로 많은 사람들이 해결책을 찾기 위해
aiohttp가 아닌 httpx를 사용을 권장하지만 근본적인 해결책은 되지 않는 것 같습니다.
이유는 미세까진아니고 조금 체감이 될 정도로 httpx.AsyncClient()가 aiohttp보다 느리게 체감됩니다.

해당 이슈를 해결하기 위한 해결책으로 baysul 이라는 유저가 다음과 같은 내용을 제시했는데
window를 사용함과 동시에 Python이 3.8 이상일 때 발생하는 현상으로
Window Selector 이벤트 루프 정책을 글로벌할게 설정하면 이를 해결할 수 있다고 합니다. 
'''

if __name__ == '__main__':
    # 헤더
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    # 변경할 URL
    long_urls = ['https://blog.naver.com', 'https://www.naver.com', 'https://www.daum.net', 'https://www.google.com', 'https://www.amazon.com']

    py_ver = int(f"{sys.version_info.major}{sys.version_info.minor}")
    if py_ver > 37 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


    # 동기 수행시간
    print('='*40 + ' 동기 수행시작 ' + '='*40)
    start = time.time()
    for long_url in long_urls:
        sync_main(long_url)
    end = time.time()
    print('='*100)
    print(f'동기 수행시간: {end - start}초\n')


    # 비동기 수행시간 (run_in_executor)
    print('='*40 + ' 비동기1 수행시작 ' + '='*40)
    start = time.time()
    for long_url in long_urls:
        asyncio.run(async_main_1(long_url))
    end = time.time()
    print('='*100)
    print(f'비동기1 수행시간: {end - start}초\n')


    # 비동기 수행시간 (코루틴만)
    print('='*40 + ' 비동기2 수행시작 ' + '='*40)
    start = time.time()
    for long_url in long_urls:
        asyncio.run(async_main_2(long_url))
    end = time.time()
    print('='*100)
    print(f'비동기2 수행시간: {end - start}초\n')
