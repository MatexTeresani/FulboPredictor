import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin 
  
url_league = 'https://football-data.co.uk/englandm.php'
url_base = 'https://football-data.co.uk/'

res = requests.get(url_league)
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.find_all('a')

for link in links: 
    href = link.get("href")
    
    if href is None: 
        continue
    else: 
        if not href.endswith('.csv'):
            continue
        else: 
            url_csv = urljoin(url_base, href)
            
            parts = href.split('/')
            name = str(parts[-1]) 
            rute = 'match-predictor/data/raw/england/' + name  
            response = requests.get(url_csv)

            with open(rute, 'wb') as archive:
                archive.write(response.content) 
                
             
                
    

        
