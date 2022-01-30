import requests
import json
# Request ee catalog
eeCatalog = requests.get('https://earthengine-stac.storage.googleapis.com/catalog/catalog.json').json()
# Get the datasets
eeDict = dict()
for dataset in eeCatalog['links']:
    if dataset['rel'] == 'child':
        response = requests.get(dataset['href'])
        if response.status_code == 200:
            dataset = requests.get(dataset['href']).json()
            if dataset['gee:type'] in ['image','image_collection']:
                if 'eo:bands' in list(dataset['summaries'].keys()):
                    bands = dataset['summaries']['eo:bands']
                    if len(bands) > 0:
                        bandsDict = dict()
                        for band in bands:
                            if 'gee:classes' in list(band.keys()):
                                if "color" in list(band['gee:classes'][0].keys()):
                                    name = band['name']
                                    colorDict = {}
                                    descriptionDict = {}
                                    for cl in band['gee:classes']:
                                        colorDict[cl['value']] = '#' + cl['color']
                                        descriptionDict[cl['value']] = cl['description']
                                    bandsDict[name] = {'color':colorDict, 'description':descriptionDict}
                        if len(bandsDict) > 0:
                            eeDict[dataset['id']] = bandsDict
# Save the list as a json file
with open('./list/ee-land-cover-datasets.json','w') as fp:
    json.dump(eeDict, fp, indent = 4, sort_keys = True)