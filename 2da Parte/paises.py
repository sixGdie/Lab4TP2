from pymongo import MongoClient
import requests as rq

client = MongoClient('mongodb://localhost:27017/')
db = client['paises_db']
collection = db['paises']

print(db.list_collection_names())

for i in range(0, 301):
    response = rq.get(
        'https://restcountries.com/v2/callingcode/' + str(i), timeout=5)
    if response.status_code == 404:
        print("No existe el codigo de pais: " + str(i))
        continue
    else:
        try:
            if collection.find_one({'codigo': i}):
                collection.update_one({'codigo': i}, {'$set': {'codigo': i, 'nombre': response.json()[
                    0]['name'], 'capital': response.json()[0]['capital'], 'region': response.json()[0]['region'], 'poblacion': response.json()[0]['population'], 'latitud': response.json()[0]['latlng'][0], 'longitud': response.json()[0]['latlng'][1]}})
                print("Se ha actualizado el país: " + str(i))
            else:
                collection.insert_one({'codigo': i, 'nombre': response.json()[
                    0]['name'], 'capital': response.json()[0]['capital'], 'region': response.json()[0]['region'], 'poblacion': response.json()[0]['population'], 'latitud': response.json()[0]['latlng'][0], 'longitud': response.json()[0]['latlng'][1]})
                print("Se ha insertado el país: " + str(i))
        except Exception as e:
            print(e)
            continue
