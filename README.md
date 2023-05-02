# Ohjelmistotekniikka

## Ostoslistasovellus

Sovelluksen avulla käyttäjät voivat luoda ostoslistoja, ja lisätä sinne haluamansa tavarat. Listoille voi lisätä tavaroita, listoja voi poistaa, ja käyttäjän luomat listat voi hakea.
 

[changelog](https://github.com/irelinna/ohte/blob/main/dokumentaatio/changelog.md)

[määrittelydokumentti](https://github.com/irelinna/ohte/blob/main/dokumentaatio/maarittelydokumentti.md)

[tuntikirjanpito](https://github.com/irelinna/ohte/blob/main/dokumentaatio/tuntikirjanpito.md)

[arkkitehtuuri](https://github.com/irelinna/ohte/blob/main/dokumentaatio/arkkitehtuuri.md)

### Ohjelman suoritus:
Asenna riippuvuudet terminaalissa komennolla: poetry install

Alusta ohjelma komennolla: poetry run invoke build

Käynnistä sovellus komennolla: poetry run invoke start

### Testaus: 
Suorita testit komennolla: poetry run invoke test

Generoi testikattavuusraportti komennolla: poetry run invoke coverage-report

### Pylint:
Suorita pylintin laatutarkistukset komennolla: poetry run invoke lint


#### Viikko 3

Tein harjoitustyötehtävistä 1, 5-7, ja olen tehnyt sovellusta eteenpäin (en vain saanut sitä vielä toimimaan tarpeeksi hyvin), palautan sitten ensi viikon deadlineen mennessä sovelluksesta perusversion.

#### Viikot 4 & 5

Olen tehnyt projektia edelleen eteenpäin, mutta atm hieman ongelmia tietokannan kanssa. Kun saan sen toimimaan, siirryn graafiseen käyttöliittymään. En jaksanut harjoitustyötehtäviä muuten paitsi suurin osa ohjelman rakenteesta pitäisi olla jo olemassa, eli tosiaan nyt vuorossa tietokanta, käyttöliittymä, testejä jne.

#### Viikko 6

Keskityn loppupalautukseen mutta olen tehnyt käyttöliittymän valmiiksi, tietokanta toimii, sovelluksen voi käynnistää ainakin omalla koneella, ja dokumentaatio on tehty sekä Entities- että Repositories-kansioiden tiedostoille. Tein arkkitehtuurikuvaukseen alustavan version ja päivitin tuntikirjanpidon, changelogin, ja määrittelydokumentin.
