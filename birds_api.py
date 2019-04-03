import requests
from pprint import pprint

species_id = input("What is the bird's latin name? ")

url = 'https://apiv3.iucnredlist.org/api/v3/species/{}?token=02454e93f9e3397b5cba8ab106ab68ebaf06614cf550ca59b9a8749d906047d7'.format(species_id)

response = requests.get(url)
redlist = response.json()

#pprint(redlist)
print(redlist['result'][0]['category'])

#url = 'https://apiv3.iucnredlist.org/api/v3/species/Ardea%20cinerea?token=02454e93f9e3397b5cba8ab106ab68ebaf06614cf550ca59b9a8749d906047d7'
