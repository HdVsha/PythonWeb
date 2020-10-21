import vk_api
import json
import requests
# Адрес api метода для запроса get
url = 'https://api.oilpriceapi.com/v1/prices/latest'
headers = {
    'Authorization': 'Token ff89ed6d4f36fa7420d146350d399722',
    'Content-Type': 'application/json'
}
# Отправляем get request (запрос GET)
response = requests.get(url=url, headers = headers)
data = response.json()
print(data)
# vk_session = vk_api.VkApi('87029862888', 'vfvjxrfgfgf12072008')
# vk_session.auth()
#
# vk = vk_session.get_api()
'''
:param
'''
#
# print(vk.wall.post(message='Hello world!'))
