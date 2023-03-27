# Määrittelydokumentti

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät pystyvät luomaan ostoslistoja.


## Käyttäjät
Sovelluksella on ainoastaan yksi käyttäjärooli eli normaali käyttäjä. Sovellukseen saatetaan lisätä suuremmilla oikeuksilla varustettu pääkäyttäjä, jos sitä tarvitaan käyttäjien hallintaan yms.


## Suunnitellut toiminnallisuudet
Ennen kirjautumista:
- Käyttäjä voi luoda käyttäjätunnuksen.
- Käyttäjätunnuksen luomiseen vaaditaan uniikki käyttäjätunnus, joka on vähintään 3 merkkiä.
- Tunnuksen luomiseen vaaditaan myös salasama
- Käyttäjätunnuksen luotuaan käyttäjä voi kirjautua sovellukseen kirjautumislomakkeella, johon syötetään käyttäjätunnus ja salasana.
- Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä

Kirjautumisen jälkeen:
- Käyttäjä voi luoda uusia ostoslistoja
- Käyttäjä voi muokata olemassa olevia ostoslistoja
- Käyttäjä voi merkitä listasta asian ostetuksi, mutta asia ei poistu listalta vaan merkitään "ostetuksi"
- Ostoslistoja voi käyttää uudelleen
- Käyttäjä voi kirjautua ulos järjestelmästä


## Jatkokehitysideat
- Käyttäjä voi tallentaa ostoslistoja "suosikeiksi" jotta kokonaisia listoja voi käyttää uudelleen
- Suosikkilistoja voi myös muokata ja tallentaa erilaisiksi
- jotain muuta, katsotaan myöhemmin
