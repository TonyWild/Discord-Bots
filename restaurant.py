import requests
import random

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('KAKAO_REST_API_TOKEN')

# "[장소] 음식점"을 검색한 후에 필터링을 적용할 것
def get_restaurant_data(region, page_num):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    params = {'query': region, 'page': page_num}
    headers = {'Authorization': f'KakaoAK {TOKEN}'}
    resp = requests.get(url, params=params, headers=headers)

    return resp.json()['documents']

def choose_random(region):
    restaurant_list = get_restaurant_data(region, 10)
    filtered_restaurant_list = [elem for elem in restaurant_list if elem['category_group_name'] == '음식점']
    return random.sample(filtered_restaurant_list, 10)

if __name__ == '__main__':
    menu = choose_random("어은동 음식점")
    print(choose_random("어은동 음식점"))
    print(menu['category_name'].split(' > ')[-1])