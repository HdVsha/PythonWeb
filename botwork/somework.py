# import vk_api
# import json
import requests
import time
import csv

def take_1000_posts():
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
        time.sleep(0.5)
    return all_posts


def file_writer(all_posts):
    with open('prepod_mipt.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        img_url = 'pass'
        for post in all_posts:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            a_pen.writerow((post['likes']['count'], post['text'], img_url))


all_posts = take_1000_posts()
file_writer(all_posts)

print(1)

