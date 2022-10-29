COOKIES = {
    'afUserId': 'cfbceabe-4652-4883-800a-e2d5424e76c2-p',
    '__woltAnalyticsId': '61f692e1-3c06-445a-9785-413717c7e8e1',
    '_ga_CP7Z2F7NFM': 'GS1.1.1664897871.1.1.1664898227.60.0.0',
    '_gcl_au': '1.1.121875411.1664898230',
    'intercom-id-qwum5ehb': '199b880b-8832-4685-93fa-45f6e1256955',
    'intercom-session-qwum5ehb': '',
    'cwc-consents': '{%22functional%22:false%2C%22analytics%22:false%2C%22marketing%22:false}',
}

HEADERS = {
    'authority': 'restaurant-api.wolt.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,he;q=0.8,ru;q=0.7',
    'app-language': 'en',
    'client-version': '1.8.19',
    'clientversionnumber': '1.8.19',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'afUserId=cfbceabe-4652-4883-800a-e2d5424e76c2-p; __woltAnalyticsId=61f692e1-3c06-445a-9785-413717c7e8e1; _ga_CP7Z2F7NFM=GS1.1.1664897871.1.1.1664898227.60.0.0; _gcl_au=1.1.121875411.1664898230; intercom-id-qwum5ehb=199b880b-8832-4685-93fa-45f6e1256955; intercom-session-qwum5ehb=; cwc-consents={%22functional%22:false%2C%22analytics%22:false%2C%22marketing%22:false}',
    'origin': 'https://wolt.com',
    'platform': 'Web',
    'referer': 'https://wolt.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'w-wolt-session-id': '61f692e1-3c06-445a-9785-413717c7e8e1',
    'x-datadog-origin': 'rum',
    'x-datadog-parent-id': '4652624790389723388',
    'x-datadog-sampling-priority': '1',
    'x-datadog-trace-id': '7195869370983322535',
    'x-wolt-web-clientid': '4d112ce598399089ea6c81cf8d3c4631',
}


def params(place_id: str):
    return {
        'place_id': f'{place_id}',
        'language': 'en',
    }
