import requests

dict_hero = {}
list_hero = ['Hulk', 'Captain America', 'Thanos']

def get_dict_hero():
    for hero in list_hero:
        url = "https://superheroapi.com/api/2619421814940190/search/"+ hero
        resp = requests.get(url)
        Hero_info = resp.json()
        Hero_intelligence = int(Hero_info['results'][0]['powerstats']['intelligence'])
        dict_hero [hero] = [Hero_intelligence]
    return dict_hero

def get_smartest_hero():
    sorted_values = sorted(dict_hero.values())
    for key, val in dict_hero.items():
        if val == sorted_values[-1]:
            return key

get_dict_hero()
print(get_smartest_hero())