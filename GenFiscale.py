
from bs4 import BeautifulSoup
import requests
import sys


if len(sys.argv) < 2:
    print("Serve il numero di codice che vuoi")
    print("Sto uscendo. Forza Roma")
else:
	numero = sys.argv[1]
	numero = int(numero)

	for x in range(numero):
		main_url = ("http://thesvalvolati.altervista.org/index.php?req=codice-fiscale-random")
		req = requests.get(main_url)
		soup = BeautifulSoup(req.text, "html.parser")
		codice = soup.find("h1")
		print (codice.get_text())