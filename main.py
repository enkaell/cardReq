import requests


def send_request():
    cookies = {
        'current_path': '9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D',
        'phonesIdent': 'c96a2b466cc1538710d165dc90a1dfa08f661e3c1c630bc2736d1530024d0b64a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%229bce703e-afb1-4fd9-b44f-e85ba57a16f0%22%3B%7D',
        'rerf': 'AAAAAGKUj5Bow6BpC4U6Ag==',
        'ipp_uid': '1653903248283/NcVLlAIIedpA9BnK/DM5CTvIo0mOyv2OBYEmoNg==',
        'rrpvid': '73',
        'rcuid': '62948f92ef1bd10001b40c85',
        'cartUserCookieIdent_v3': '4eba3d1331a8ba1378c8784630864bb80fbf283fbb05d80708ea945e367f7866a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2214624fe3-9634-3199-a3b8-5b384c04a69e%22%3B%7D',
        '_gcl_au': '1.1.1708355435.1653903255',
        '_ym_uid': '1653903255845720609',
        '_ym_d': '1653903255',
        'tmr_lvid': '8b5f73b43df275cbcee5744344e9a45c',
        'tmr_lvidTS': '1653903255199',
        '__ttl__widget__ui': '1653903261851-85b9666801d5',
        'cookieImagesUploadId': 'f81ba7e45fb53d1208eef8a6901187d62ec2dc5e773cffc999b3f5c52bcddb47a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22cookieImagesUploadId%22%3Bi%3A1%3Bs%3A36%3A%22a47432df-bd73-4354-bdac-af3b8bceb26d%22%3B%7D',
        'lang': 'ru',
        'PHPSESSID': '96e4ece36a194fa4029f77d62732f0a4',
        '_csrf': '8714c26b7ea5a74b24ec0bb3d126b7c7ec12fdc84ebfb0472b6da1f018aea47da%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22B9MLvoTNhgurBzKHuVgHgkrqP1Wuu-o5%22%3B%7D',
        '_gid': 'GA1.2.1695307137.1655815321',
        '_gaexp': 'GAX1.2.F5r0LoWFQuaGkKl-pfLADg.19228.0',
        '_ym_isad': '1',
        'flixgvid': 'flix9b2fc520000000.49133203',
        'ipp_key': 'v1655835272582/v33947245ba5adc7a72e273/SF1p6jaDmAn6wLHpPWrbkQ==',
        '_ym_visorc': 'b',
        'tmr_detect': '1%7C1655836069551',
        '_ga': 'GA1.2.440090287.1653903250',
        'tmr_reqNum': '78',
        'dnsauth_csrf': 'fd41deb1bbb1a6d6407c7a8ed9e750620c52bf11b309a6be821ea897ddce85e3a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22dnsauth_csrf%22%3Bi%3A1%3Bs%3A36%3A%229ebd3d37-291f-46ee-9c55-4d8dc73d2ca9%22%3B%7D',
        '_ga_FLS4JETDHW': 'GS1.1.1655835270.3.1.1655836591.0',
        'rr-testCookie': 'testvalue',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9,es;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D; phonesIdent=c96a2b466cc1538710d165dc90a1dfa08f661e3c1c630bc2736d1530024d0b64a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%229bce703e-afb1-4fd9-b44f-e85ba57a16f0%22%3B%7D; rerf=AAAAAGKUj5Bow6BpC4U6Ag==; ipp_uid=1653903248283/NcVLlAIIedpA9BnK/DM5CTvIo0mOyv2OBYEmoNg==; rrpvid=73; rcuid=62948f92ef1bd10001b40c85; cartUserCookieIdent_v3=4eba3d1331a8ba1378c8784630864bb80fbf283fbb05d80708ea945e367f7866a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2214624fe3-9634-3199-a3b8-5b384c04a69e%22%3B%7D; _gcl_au=1.1.1708355435.1653903255; _ym_uid=1653903255845720609; _ym_d=1653903255; tmr_lvid=8b5f73b43df275cbcee5744344e9a45c; tmr_lvidTS=1653903255199; __ttl__widget__ui=1653903261851-85b9666801d5; cookieImagesUploadId=f81ba7e45fb53d1208eef8a6901187d62ec2dc5e773cffc999b3f5c52bcddb47a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22cookieImagesUploadId%22%3Bi%3A1%3Bs%3A36%3A%22a47432df-bd73-4354-bdac-af3b8bceb26d%22%3B%7D; lang=ru; PHPSESSID=96e4ece36a194fa4029f77d62732f0a4; _csrf=8714c26b7ea5a74b24ec0bb3d126b7c7ec12fdc84ebfb0472b6da1f018aea47da%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22B9MLvoTNhgurBzKHuVgHgkrqP1Wuu-o5%22%3B%7D; _gid=GA1.2.1695307137.1655815321; _gaexp=GAX1.2.F5r0LoWFQuaGkKl-pfLADg.19228.0; _ym_isad=1; flixgvid=flix9b2fc520000000.49133203; ipp_key=v1655835272582/v33947245ba5adc7a72e273/SF1p6jaDmAn6wLHpPWrbkQ==; _ym_visorc=b; tmr_detect=1%7C1655836069551; _ga=GA1.2.440090287.1653903250; tmr_reqNum=78; dnsauth_csrf=fd41deb1bbb1a6d6407c7a8ed9e750620c52bf11b309a6be821ea897ddce85e3a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22dnsauth_csrf%22%3Bi%3A1%3Bs%3A36%3A%229ebd3d37-291f-46ee-9c55-4d8dc73d2ca9%22%3B%7D; _ga_FLS4JETDHW=GS1.1.1655835270.3.1.1655836591.0; rr-testCookie=testvalue',
        'Origin': 'https://www.dns-shop.ru',
        'Referer': 'https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/no-referrer',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.143 YaBrowser/22.5.0.1878 Yowser/2.5 Safari/537.36',
        'X-CSRF-Token': 'UhBKrecgSkNVp3Tr2qSYo9tmv0A1OkbcbNep5ptsI8EQKQfhkU8eDT3AAZmY3tPrrjDYCFJRNK085v6T7kFM9A==',
        'X-Requested-With': 'XMLHttpRequest',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    params = {
        'cityId': '10',
        'langId': 'ru',
        'v': '2',
    }

    data = 'data={"type":"product-buy","containers":[{"id":"as-d8jxYo","data":{"id":"11fc149f-2d51-11eb-a211-00155d03332b"}},{"id":"as-qH7SPC","data":{"id":"fbb7f1aa-27d1-11eb-a211-00155d03332b"}},{"id":"as-4ejqHX","data":{"id":"ed52cedb-70d9-11eb-a221-00155d03332b"}},{"id":"as-lNccnj","data":{"id":"6db4f449-90ef-11eb-a240-00155dbd7607"}},{"id":"as-FlbNG6","data":{"id":"054b9723-2d50-11eb-a211-00155d03332b"}},{"id":"as-env-Jg","data":{"id":"5eb27721-1f71-11ec-8ef4-00155d8ed20b"}},{"id":"as-_WOtI1","data":{"id":"d8e99380-3a09-11eb-a211-00155d03332b"}},{"id":"as-6jpOsH","data":{"id":"dc2db920-79b1-11ec-8f63-00155d8ed20b"}},{"id":"as-MXUi07","data":{"id":"361c6774-70d9-11eb-a221-00155d03332b"}},{"id":"as-dMYu3e","data":{"id":"0db93359-d1d0-11ec-8fba-00155d8ed20c"}},{"id":"as-72HyzZ","data":{"id":"923e1507-2fc1-11eb-a211-00155d03332b"}},{"id":"as-fKpAyh","data":{"id":"2829e8aa-2f7e-11eb-a211-00155d03332b"}},{"id":"as-HcMsSq","data":{"id":"07ba9557-6f51-11eb-a21f-00155d03332b"}},{"id":"as-m5zq6t","data":{"id":"a46600d8-7751-11eb-a225-00155d42eb06"}},{"id":"as-2-yIDc","data":{"id":"6ba72f0f-6947-11ec-8f53-00155d8ed20b"}},{"id":"as-1pscVO","data":{"id":"b87d194a-e538-11ec-8fcc-00155d8ed20b"}},{"id":"as-ZQO4M0","data":{"id":"c688624a-c743-11eb-a275-00155dbd7634"}},{"id":"as-CQdYET","data":{"id":"99ad67d4-27d2-11eb-a211-00155d03332b"}}]}'

    response = requests.post('https://www.dns-shop.ru/ajax-state/product-buy/', params=params, cookies=cookies,
                             headers=headers, data=data)
    print(response.json().get('data').get('states')[0])


if __name__ == '__main__':
    send_request()
