import requests as rq
import mysql.connector as mc

db = mc.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="tp2",
    auth_plugin="mysql_native_password"
)

paises = []
cursor = db.cursor()

for i in range(0, 301):
    response = rq.get(
        'https://restcountries.com/v2/callingcode/' + str(i), timeout=5)
    if response.status_code == 404:
        print("No existe el codigo de pais: " + str(i))
        continue
    try:
        cursor.execute("INSERT INTO pais (codigo, nombre, capital, region, poblacion, latitud, longitud) VALUES (%s, %s, %s, %s, %s, %s, %s)", (response.json()[0]['callingCodes'][0], response.json()[
                       0]['name'], response.json()[0]['capital'], response.json()[0]['region'], response.json()[0]['population'], response.json()[0]['latlng'][0], response.json()[0]['latlng'][1]))
        db.commit()
    except:
        print("Error al insertar el pais: " + str(i))
        continue
