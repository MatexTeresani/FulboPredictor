import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin 
import os 
url_league = 'https://football-data.co.uk/englandm.php'
url_base = 'https://football-data.co.uk/'
cont_legues = 4 # cambiar en caso de buscar otras ligas 

res = requests.get(url_league)
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.find_all('a')
season_names = soup.find_all('i')
contSeason = 1 
contLegue = 0  
for season_name in season_names: 
    sName = season_name.get_text()
    if contSeason == 2: 
        firstSeason = str(sName)
        firstSeason = firstSeason.replace("/", "-")
    elif contSeason == 3: 
        secondSeason = str(sName)
        secondSeason = secondSeason.replace("/", "-")

    contSeason += 1  
    
print(os.getcwd())
print(firstSeason)
print(secondSeason)
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
            contLegue += 1 
            if contLegue <= cont_legues:     
                rute = 'match-predictor/data/raw/england/'+firstSeason+'/' + name
                os.makedirs('match-predictor/data/raw/england/'+firstSeason, exist_ok = True) 
            elif contLegue > cont_legues: 
                rute = 'match-predictor/data/raw/england/'+secondSeason+'/' + name 
                os.makedirs('match-predictor/data/raw/england/'+secondSeason, exist_ok = True)
            response = requests.get(url_csv)
            
              
            with open(rute, 'wb') as archive:
                archive.write(response.content) 
                
             
                
    

        
