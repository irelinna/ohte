# Määrittelydokumentti

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät pystyvät luomaan ostoslistoja.


## Käyttäjät
Sovelluksella on ainoastaan yksi käyttäjärooli eli normaali käyttäjä. 


## Suunnitellut toiminnallisuudet
Ennen kirjautumista:
- Käyttäjä voi luoda käyttäjätunnuksen.
- Käyttäjätunnuksen luomiseen vaaditaan uniikki käyttäjätunnus, joka on vähintään 3 merkkiä.
- Tunnuksen luomiseen vaaditaan myös salasama
- Käyttäjätunnuksen luotuaan käyttäjä voi kirjautua sovellukseen kirjautumislomakkeella, johon syötetään käyttäjätunnus ja salasana.
- Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä

Kirjautumisen jälkeen:
- Käyttäjä voi luoda uusia ostoslistoja
- Käyttäjä voi lisätä uusia tavaroita ostoslistalle
- Käyttäjä voi poistaa ostoslistan
- Käyttäjä voi kirjautua ulos järjestelmästä
