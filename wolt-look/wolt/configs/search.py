import requests

COOKIES = {
    '__woltAnalyticsId': 'c9c17745-aaab-45f8-b395-08047d52a3c3',
    '_gcl_au': '1.1.321215117.1666367100',
    'intercom-id-qwum5ehb': 'b2009373-08a0-4aa5-ad5b-8397d52db7ff',
    'intercom-session-qwum5ehb': '',
    'cwc-consents': '{%22analytics%22:true%2C%22functional%22:true%2C%22marketing%22:true}',
    '__woltUid': 'cbd75795-78e0-4bf2-ac4e-6a117a5d945e',
    '_gid': 'GA1.2.1043552880.1666367107',
    '_fbp': 'fb.1.1666367107246.1969963086',
    '_ga': 'GA1.2.1472734533.1666367107',
    '_gat_UA-56809017-2': '1',
    '_ga_CP7Z2F7NFM': 'GS1.1.1666367107.1.1.1666367166.1.0.0',
}

HEADERS = {
    'authority': 'restaurant-api.wolt.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en;q=0.9',
    'app-language': 'en',
    'client-version': '1.9.7',
    'clientversionnumber': '1.9.7',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__woltAnalyticsId=c9c17745-aaab-45f8-b395-08047d52a3c3; _gcl_au=1.1.321215117.1666367100; intercom-id-qwum5ehb=b2009373-08a0-4aa5-ad5b-8397d52db7ff; intercom-session-qwum5ehb=; cwc-consents={%22analytics%22:true%2C%22functional%22:true%2C%22marketing%22:true}; __woltUid=cbd75795-78e0-4bf2-ac4e-6a117a5d945e; _gid=GA1.2.1043552880.1666367107; _fbp=fb.1.1666367107246.1969963086; _ga=GA1.2.1472734533.1666367107; _gat_UA-56809017-2=1; _ga_CP7Z2F7NFM=GS1.1.1666367107.1.1.1666367166.1.0.0',
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
    'w-wolt-session-id': 'c9c17745-aaab-45f8-b395-08047d52a3c3',
    'x-datadog-origin': 'rum',
    'x-datadog-parent-id': '2006321672944045092',
    'x-datadog-sampling-priority': '1',
    'x-datadog-trace-id': '7352337665276439294',
    'x-wolt-web-clientid': '98e6d4153778f65e8d1c98c5da94035c',
}

FILTER_PARAMS = {
    'unit_prices': 'true',
    'show_weighted_items': 'true',
}
FILTER_HEADERS = {
    'authority': 'restaurant-api.wolt.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en;q=0.9',
    'app-language': 'en',
    'client-version': '1.9.7',
    'clientversionnumber': '1.9.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gcl_au=1.1.321215117.1666367100; intercom-id-qwum5ehb=b2009373-08a0-4aa5-ad5b-8397d52db7ff; intercom-session-qwum5ehb=; cwc-consents={%22analytics%22:true%2C%22functional%22:true%2C%22marketing%22:true}; __woltUid=cbd75795-78e0-4bf2-ac4e-6a117a5d945e; _gid=GA1.2.1043552880.1666367107; _fbp=fb.1.1666367107246.1969963086; ravelinDeviceId=rjs-7839a549-5a1f-4c7a-8cb9-f9b6dfa053eb; ravelinSessionId=rjs-7839a549-5a1f-4c7a-8cb9-f9b6dfa053eb:eb1da015-79e4-4c73-9e2b-114edf4df51e; rskxRunCookie=0; rCookie=an3sg3qq93f2ufalr0an3pl9jxn1eg; _ga=GA1.2.1472734533.1666367107; __woltAnalyticsId=a6183e58-38f1-4ec8-95d6-c4fb94a2ea79; lastRskxRun=1666463011318; _gat_UA-56809017-2=1; _ga_CP7Z2F7NFM=GS1.1.1666465825.6.1.1666465827.58.0.0',
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
    'w-wolt-session-id': '697d98cc-8941-4597-9f87-71abf38f91c6',
    'x-datadog-origin': 'rum',
    'x-datadog-parent-id': '8089459912861592263',
    'x-datadog-sampling-priority': '1',
    'x-datadog-trace-id': '7739726507511174901',
    'x-wolt-web-clientid': '98e6d4153778f65e8d1c98c5da94035c',
}
FILTER_COOKIES = {
    '_gcl_au': '1.1.321215117.1666367100',
    'intercom-id-qwum5ehb': 'b2009373-08a0-4aa5-ad5b-8397d52db7ff',
    'intercom-session-qwum5ehb': '',
    'cwc-consents': '{%22analytics%22:true%2C%22functional%22:true%2C%22marketing%22:true}',
    '__woltUid': 'cbd75795-78e0-4bf2-ac4e-6a117a5d945e',
    '_gid': 'GA1.2.1043552880.1666367107',
    '_fbp': 'fb.1.1666367107246.1969963086',
    'ravelinDeviceId': 'rjs-7839a549-5a1f-4c7a-8cb9-f9b6dfa053eb',
    'ravelinSessionId': 'rjs-7839a549-5a1f-4c7a-8cb9-f9b6dfa053eb:eb1da015-79e4-4c73-9e2b-114edf4df51e',
    'rskxRunCookie': '0',
    'rCookie': 'an3sg3qq93f2ufalr0an3pl9jxn1eg',
    '_ga': 'GA1.2.1472734533.1666367107',
    '__woltAnalyticsId': 'a6183e58-38f1-4ec8-95d6-c4fb94a2ea79',
    'lastRskxRun': '1666463011318',
    '_gat_UA-56809017-2': '1',
    '_ga_CP7Z2F7NFM': 'GS1.1.1666465825.6.1.1666465827.58.0.0',
}


def contains(name, requested):
    """
    Find if product name includes any mention of the requested item
    :param name: The name of the item in the restaurant
    :param requested: The requested product query
    :return:
    """
    # name = name.encode('utf-8')  # TODO: Check for hebrew problems
    for word in name.split(" "):
        for sub_word in requested.split(" "):
            if word == sub_word:
                return True


def find_meal(items_list: dict, price: int, product: str):
    """
    Find the product we were searching for and try to filter it by the given price
    :param items_list:
    :param price:
    :param product:
    :return: Returns the list of the filtered restauratnt
    """
    filtered = {}
    for name, information in items_list.items():
        response = requests.get(f"https://restaurant-api.wolt.com/v4/venues/slug/{information['slug']}/menu",
                                params=FILTER_PARAMS,
                                cookies=FILTER_COOKIES,
                                headers=FILTER_HEADERS)
        if response.status_code == 200 and response.json():
            # First find the corresponding meals
            meals = [food_item for food_item in response.json()["items"]
                     if contains(food_item["name"], product)]  # Find meals matching to requested product
            if meals:
                price_filter = [food_item for food_item in meals if food_item["baseprice"] / 100 <= price]
                if price_filter:
                    information["meals"] = price_filter
                    filtered[name] = information
    return filtered


def apply_filters(filtered: dict, filters: dict, product=None) -> dict:
    """

    :param product:
    :param filtered: Open restaurants that deliver to the location
    :param filters: Dict of filters and their values (meal_price, restaurant_rating, delivery_time, max_delivery)
    :return:
    """
    if "restaurant_rating" in filters:
        filtered = {k: v for k, v in filtered.items()
                    if v["rating"]["score"] >= filters["restaurant_rating"]}
    if "delivery_time" in filters:
        filtered = {k: v for k, v in filtered.items()
                    if int(v["estimate_range"].split('-')[1]) <= filters["delivery_time"]}
    if "max_delivery" in filters:
        filtered = {k: v for k, v in filtered.items()
                    if v["delivery_price_int"] / 100 <= filters["max_delivery"]}
    if "meal_price" in filters:
        filtered = find_meal(items_list=filtered, price=filters["meal_price"], product=product)

    return filtered


def filter_items(items_list: list, filters=None, product=None) -> dict:
    """Remove restaurants that are not delivering, and return only needed properties"""
    filtered = {}
    for item in items_list:
        if "overlay" in item:  # or item["sorting"]["sortables"][2]["value"] == 0:
            continue

        filtered[item["title"]] = item["venue"]
    print(f"\t[*] (1) Reduced search results from {len(items_list)} to {len(filtered)}")

    if filters and filtered:
        filtered = apply_filters(filtered=filtered, filters=filters, product=product)
        print(f"\t[*] (2) After filters, results reduced from {len(items_list)} to {len(filtered)}")
    return filtered


def json(q: str, lat: str, lan: str):
    return {
        'q': q,
        'lat': lat,
        'lon': lan,
        'sorting_and_filtering_v2': None
    }
