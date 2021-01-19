import json
import os
import requests

from urllib.parse import urljoin

cr_token = os.environ.get('CR_TOKEN')
player_tag = os.environ.get('PLAYER_TAG')

def get_chests_info(cr_token, player_tag):
    base_url = urljoin('https://api.clashroyale.com/v1/players/', player_tag)
    url = urljoin(base_url, 'upcomingchests')
    headers = {
        "cache-control": "max-age=60",
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer  %s" % cr_token}
    r = requests.get(url, headers=headers)
    data = r.json()
    return data

def main(cr_token, player_tag):
    info = get_chests_info(cr_token, player_tag)

    chests_dic = {'Silver Chest': '銀の宝箱', 'Golden Chest': '金の宝箱', 'Giant Chest': '巨大宝箱',
                'Magical Chest': '魔法の宝箱', 'Epic Chest': 'スーパーレア宝箱', 
                'Mega Lightning Chest': 'メガライトニング宝箱', 'Legendary Chest': 'ウルトラレア宝箱'}

    show_list = [chests_dic[info['items'][i]['name']] for i in range(5)]
    
    print(*show_list)
