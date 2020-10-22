import requests
import json

def take_1000_posts():
    # count is 100 bc vk only allows to request 100 items at once --- that's why it is cycle
    token = 'd06b0e85d06b0e85d06b0e852cd01f8b05dd06bd06b0e858ffb25e7d3f0e3c1d1593e5d'
    offset = 0
    count = 100
    all_posts = []
    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': 5.124,
                                    'domain': 'prepod_mipt',
                                    'count': count,
                                    'offset': offset
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_writer(all_posts):
    with open('prepod_mipt.txt', 'w') as file:
        for post in all_posts:
            try:
                file.writelines(post['text'])
            except:
                pass



