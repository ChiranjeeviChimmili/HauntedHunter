import requests
from bs4 import BeautifulSoup

def state_info(state):
    url = 'http://theshadowlands.net/places/' + state + ".htm"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for paragraph in soup.find_all("p"):
        if '-' in paragraph.get_text():
            para_text = paragraph.get_text()
            split_soup = para_text.split('\n\n')
    return split_soup

def find_city(city, state):
    haunted_list = []
    locations = state_info(state)
    for i in locations:
        if get_city(i) == city:
            haunted_list.append(i)
    return haunted_list

def find_all_cities(soup):
    city_list = []
    for i in soup:
        if i:
            city_list.append(get_city(i))
    return list(filter(None, city_list))

def get_city(haunted_place):
    city = haunted_place.split("-")[0]
    return city.strip()

def get_name(haunted_place):
    name = haunted_place.split("-")[1]
    name2 = haunted_place.split("-")[2]
    name2check = name2.split() 
    if len(name2check) <= 7:
        return name.strip() + " " + name2.strip()
    return name.strip()

def get_description(haunted_place):
    n = 2
    desc = haunted_place.split("-")[n]
    desccheck = desc.split()
    if len(desccheck) <= 7:
        n += 1
    desc = haunted_place.split("-")[n: ]
    string = ""
    for i in desc:
        i = i.strip()
        string += i
    if type(warning(string)) == str:
        return warning(string) + "\n" + string
    return string

def warning(description):
    trespassing = ["trespassing", "trespassers", "prosecuted", "tresspassing."]
    torn_down = ["torn down", "demolished"]
    if (any(warning in description for warning in trespassing)):
        print("***TRESPASSING WARNING***")
    if (any(warning in description for warning in torn_down)):
        print("***TORN DOWN OR POSSIBLY TORN DOWN***")