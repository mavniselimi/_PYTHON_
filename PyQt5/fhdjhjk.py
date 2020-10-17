
import requests
tl=float(input("TL'yi giriniz."))
dolar=float(input("Doları giriniz."))
api_key="5602d650ec7fd2264838303218664d93"
url = "http://data.fixer.io/api/latest?access_key=" + api_key
limkk=requests.get(url)
infos = limkk.json()
dolartotl = infos["rates"]["TRY"]
tltodolar = infos["rates"]["USD"]
tl_dolar=tl*(tltodolar/dolartotl)
dolar_tl=dolar*(dolartotl/tltodolar)
print(tl,"TL",round(tl_dolar,2),"dolardır.")
print(dolar,"dolar",round(dolar_tl,2),"TL'dir.")
