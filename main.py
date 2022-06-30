import requests
from requests import Session


def send_request():
    # testcookies@mail.ru
    # prettyflowforany
    sess: Session = requests.Session()
    print(sess.headers)
    cookies = {
        'ipp_uid': '1653903248283/NcVLlAIIedpA9BnK/DM5CTvIo0mOyv2OBYEmoNg==',
        'lang': 'ru',
        '_csrf': '8714c26b7ea5a74b24ec0bb3d126b7c7ec12fdc84ebfb0472b6da1f018aea47da%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22B9MLvoTNhgurBzKHuVgHgkrqP1Wuu-o5%22%3B%7D'
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9,es;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'https://www.dns-shop.ru',
        'Referer': 'https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/no-referrer',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.143 YaBrowser/22.5.0.1878 Yowser/2.5 Safari/537.36',
        'X-CSRF-Token': 'UhBKrecgSkNVp3Tr2qSYo9tmv0A1OkbcbNep5ptsI8EQKQfhkU8eDT3AAZmY3tPrrjDYCFJRNK085v6T7kFM9A==',
        'X-Requested-With': 'XMLHttpRequest',
        'content-type': 'application/x-www-form-urlencoded'
    }

    params = {
        'cityId': '10',
        'langId': 'ru',
        'v': '2',
    }

    data = 'data={"type":"product-buy","containers":[{"id":"as-HnUKGn","data":{' \
           '"id":"bd31a687-b5a7-11ec-a28c-00155dd2ff41"}},{"id":"as-K4uHY4","data":{' \
           '"id":"6e94872d-ddbd-11ec-a28c-00155dd2ff41"}},{"id":"as-5atcaE","data":{' \
           '"id":"5a7b4c6d-0bc3-11ec-a2b0-00155dfc8232"}},{"id":"as-ielf0l","data":{' \
           '"id":"9fb53308-083d-11e6-94d3-00155d033307"}},{"id":"as-WTvdyX","data":{' \
           '"id":"9a003379-891d-11ea-a20f-00155d03332b"}},{"id":"as-XxQBEb","data":{' \
           '"id":"d03b6076-3927-11e7-939d-00155d03330d"}},{"id":"as-DzIQ_E","data":{' \
           '"id":"8d99fc87-ddcf-11ec-a28c-00155dd2ff41"}},{"id":"as-B521L8","data":{' \
           '"id":"8d99fc81-ddcf-11ec-a28c-00155dd2ff41"}},{"id":"as-bbTxM2","data":{' \
           '"id":"34addc53-49e6-11e4-8326-005056a4699b"}},{"id":"as-7PpyKp","data":{' \
           '"id":"66b8a6c7-3850-11ec-8f1a-00155d8ed20c"}},{"id":"as---dVNL","data":{' \
           '"id":"70b6f17f-c365-11e7-938d-00155d03330d"}},{"id":"as-m7rd0l","data":{' \
           '"id":"e5fcb990-de4e-11e7-a776-00155d03330d"}},{"id":"as-Biw-Sr","data":{' \
           '"id":"4e2d233d-ce28-11e5-bc54-00155d033307"}},{"id":"as-tL1mqe","data":{' \
           '"id":"027c0543-5631-11ec-8f41-00155d8ed20b"}},{"id":"as-ns3wxk","data":{' \
           '"id":"73667432-f768-11e8-a208-00155df1b805"}},{"id":"as--pwTJR","data":{' \
           '"id":"8c12d3e8-2d96-11ec-8f06-00155d8ed20b"}},{"id":"as-LPC0dl","data":{' \
           '"id":"6aae0cda-a22f-11e5-aebf-00155d03361b"}},{"id":"as-syLYWm","data":{' \
           '"id":"622cfa0b-428d-11ec-8f29-00155d8ed20b"}}]} '

    response = requests.post('https://www.dns-shop.ru/ajax-state/product-buy/', params=params, cookies=cookies,
                             headers=headers, data=data)
    states = response.json().get('data').get('states')
    resp = sess.post('https://www.dns-shop.ru/ajax-state/product-buy/?cityId=10&langId=ru&v=2', headers=headers)
    print(resp.cookies.get_dict())
    print(data_performer(states))


def data_performer(states):
    recs = []
    for i in states:
        recs.append({"name": i['data']['name'], 'default_price': i['data']['price']['current'],
                     'sale_price': i['data']['price']['sale'] if 'sale' in i['data']['price'] else 0})
    return recs


if __name__ == '__main__':
    send_request()
