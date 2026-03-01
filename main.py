from sqlalchemy.orm import Session
from db_init import University, Domain, WebPage, engine
import requests

# Tentei utilizar o endpoint `/search`, conforme indicado no repositório oficial da API (https://github.com/Hipo/university-domains-list-api), para buscar universidades de todos os países. No entanto, percebi que ele não retorna todos os registros sem um filtro específico. Por isso, optei por manter o filtro para o Brasil, garantindo que a busca funcione
url = "http://universities.hipolabs.com/search?country=Brazil"
response = requests.get(url)
response.raise_for_status()
unis = response.json()

with Session(engine) as session:
    for uni in unis:
        u = University(
            name=uni.get('name'),
            country=uni.get('country'),
            state_province=uni.get('state-province'),
            alpha_two_code=uni.get('alpha_two_code')
        )
        session.add(u)
        session.flush() 

        for domain in uni.get('domains', []):
            session.add(Domain(university_id=u.id, domain=domain))
        for web_page in uni.get('web_pages', []):
            session.add(WebPage(university_id=u.id, web_page=web_page))

    session.commit()