import requests
import json

API_KEY = "RGAPI-571f8..."


def parse_bytes(byte_obj):
    bytes_content = byte_obj
    string_content = bytes_content.decode('utf-8')
    dictionary = json.loads(string_content)
    return dictionary


def save_to_text_file(l):
    with open('puuid_list.txt', 'w') as f:
        for item in l:
            f.writelines(item + '\n')


response = requests.get(
    'https://br1.api.riotgames.com/tft/league/v1/challenger',
     headers={
        "X-Riot-Token": "RGAPI-571f86..."
     }
)

dictionary = parse_bytes(response.content)

summoner_id_list = []
puuid_list = []
for item in dictionary['entries']:
    summoner_id = item['summonerId']
    summoner_id_list.append(summoner_id)

    response2 = requests.get(
        'https://br1.api.riotgames.com/lol/summoner/v4/summoners/{}'.format(summoner_id),
        headers={
            "X-Riot-Token": "RGAPI-571f86..."
        }
    )
    d2 = parse_bytes(response2.content)
    puuid_list.append(d2['puuid'])

save_to_text_file(puuid_list)

# Remove duplicates from list:
# clean_list = list(set(l))
