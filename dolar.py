# WebScrapping-dolar

import requests

from bs4 import BeautifulSoup       

  headers = {'User-Agent':('Mozila/5.0 Windows NT 10.0;WOW64;Trident/7.0; rv:11.0)'}

     page = requests.get("https://dolarhoje.com/"headers=header) #Acessar site

 print(page.content)

   soup = BeautifulSoup(page.content, 'html.parser')

     atributos = {'class': 'id=cotação'}
        
        respostas = soup.find_all("div", attrs=atributos)
  
  print(Valor_dólar.text)
