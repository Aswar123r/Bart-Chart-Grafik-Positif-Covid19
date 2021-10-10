from matplotlib import pyplot as plt
from matplotlib import style
import json
import requests

style.use('ggplot')
Kode_provinsi = []
jumlah_positif =[]

def grafik():
    endpoint = 'https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
    response = requests.get(endpoint)
    data = json.loads(response.text)
    return (data)

data = grafik()

nomor = 0
x = []


for covid in data['features']:
    x.append(nomor)
    Kode_provinsi.append(covid['attributes']['Kode_Provi'])
    jumlah_positif.append(covid['attributes']['Kasus_Posi'])
    nomor = nomor + 1


Kode_provinsi.pop()
jumlah_positif.pop()
x.pop()

y = jumlah_positif

fig, ax = plt.subplots()

ax.bar(x, y, align='center')

ax.set_title("Kasus positif di setiap provinsi")
ax.set_ylabel('jumlah')
ax.set_xlabel('Kode Provinsi')
ax.set_xticks(x)
ax.set_xticklabels((Kode_provinsi))

plt.show()







