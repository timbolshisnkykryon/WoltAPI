import requests
from configs import suggestions, place_information, restaurants, search
import urllib.parse


class Wolt:
    def __init__(self, address=None, lat_lan=None):
        self.address = address
        self.lat_lan = lat_lan
        self.place_id = None
        self.cookies = None
        self.ready = False
        self.error = None

        if address:
            self.setup()

    def setup(self):
        print("[*] Setting up your place information...")

        self.get_place_suggestions()
        assert self.place_id is not None
        print(f"\t[+] Got place id ({self.place_id})")

        self.place_information_by_id()
        assert self.lat_lan is not None
        print(f"\t[+] Got place coordinates {self.lat_lan}")

        print(f"[*] Wolt search is ready for further actions\n")
        self.ready = True

    def get_place_suggestions(self):
        safe_string = urllib.parse.quote_plus(self.address)

        response = requests.get(
            f'https://restaurant-api.wolt.com/v1/google/places/autocomplete/json?input={safe_string}&language=en&types=geocode&location=32.087,34.787&radius=100000',
            cookies=suggestions.COOKIES, headers=suggestions.HEADERS)
        if response.status_code == 200 and response.json() and response.json()['predictions']:
            place_id = response.json()['predictions'][0]['place_id']
            self.place_id = place_id

    def place_information_by_id(self):
        response = requests.get('https://restaurant-api.wolt.com/v1/google/geocode/json',
                                params=place_information.params(self.place_id),
                                cookies=place_information.COOKIES,
                                headers=place_information.HEADERS)
        if response.status_code == 200 and response.json() and response.json()['results']:
            place_location = response.json()['results'][0]['geometry']['location']
            self.lat_lan = (place_location['lat'], place_location['lng'])
            self.cookies = response.cookies

    def restaurant_by_location(self):
        response = requests.get('https://restaurant-api.wolt.com/v1/pages/front',
                                params=restaurants.params(self.lat_lan(0), self.lat_lan(1)),
                                cookies=restaurants.COOKIES if not self.cookies else self.cookies,
                                headers=restaurants.HEADERS)

        print(f"\n Received {len(response.json()['sections'][1]['items'])} popular restaurants by location")

    def search_for_product(self, product_name):
        print(f"[*] Searching for '{product_name}' in wolt search...")
        response = requests.post('https://restaurant-api.wolt.com/v1/pages/search',
                                 cookies=search.COOKIES,
                                 headers=search.COOKIES if not self.cookies else self.cookies,
                                 json=search.json(q=product_name, lat=self.lat_lan[0], lan=self.lat_lan[1]))
        if response.status_code == 200 and response.json() and response.json()['sections']:
            filtered_items = search.filter_items(response.json()['sections'][0]['items'])
            print(f"\t[+] Received {len(filtered_items)} restaurants that sell that product")
            return filtered_items
        return None

    def filtered_search_for_product(self, product_name, filters=None):

        print(f"[*] Searching for '{product_name}' in wolt search with the following filters ({filters.keys()})...")
        response = requests.post('https://restaurant-api.wolt.com/v1/pages/search',
                                 cookies=search.COOKIES,
                                 headers=search.COOKIES if not self.cookies else self.cookies,
                                 json=search.json(q=product_name, lat=self.lat_lan[0], lan=self.lat_lan[1]))
        if response.status_code == 200 and response.json() and response.json()['sections']:
            filtered_items = search.filter_items(items_list=response.json()['sections'][0]['items'],
                                                 filters=filters,
                                                 product=product_name)
            print(f"\t[+] Received {len(filtered_items)} restaurants that sell that product")
            return filtered_items
        return None

if "__main__" == __name__:
    w = Wolt("Herzliya")
    if w.ready:
        w.search_for_product("burger")
    # print(w.restaurant_by_location(w.place_information_by_id(w.get_place_suggestions())))
