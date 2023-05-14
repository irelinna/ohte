# Käyttöohje

## Sovelluksen käyttöönotto
Lataa projektin viimeisimmän releasen lähdekoodi.

Sovellus tallentaa tiedot tiedostoihin, jotka luodaan automaattisesti data-hakemistoon, jos niitä ei ole. 
Dokumentista .env voi muokata käytettävien tiedostojen nimiä tarvittaessa. Oletusarvoisesti tiedoston sisältö on:

DATABASE_FILENAME=database.sqlite

jossa database.sqlite on tietokantatiedosto.

#### Riippuvuuksien asennus
Asenna riippuvuudet terminaalissa komennolla: poetry install

Alusta ohjelma komennolla: poetry run invoke build

Käynnistä sovellus komennolla: poetry run invoke start

## Käyttöliittymä ja toiminnot
Käyttöliittymä näyttää sovelluksen käynnistämisen jälkeen tältä:

![käyttöliittymä](https://github.com/irelinna/ohte/assets/101975853/9bf37d64-c2f4-4ba3-b195-d0974c979057)

- Käyttäjän tulee kirjoittaa toivomansa komennon numeron, jolloin sovellus suorittaa komennon. Jos annettu komentu ei ole olemassa, ilmoittaa sovellus tästä ja tulostaa ohjeet uudestaan.
- Käyttäjän tulee olla kirjautunut sisään (komento 1) luodakseen listan, ja jos ei ole, ilmoittaa sovellus tästä. 
- Jos käyttäjä ei ole aiemmin luonut käyttäjätunnusta, tulee sellainen luoda komennolla 2. Sovellus ilmoittaa jos valittu käyttäjätunnus on jo käytössä.
- Käyttäjän luomisen ja kirjautumisen jälkeen käyttäjä pystyy luomaan listan komennolla 3. Sovellus kysyy uudelle listalle annettavaa nimeä, ja siihen lisättäviä tavaroita.
- Listaan voi myöhemmin lisätä lisää tavaroita komennolla 4.
- Komennolla 5 käyttäjä pystyy etsimään listan nimen perusteella, jolloin sovellus tulostaa listassa olevat tavarat.
- Komennolla 6 käyttäjä voi poistaa listan. 
- Käyttäjä voi kirjautua ulos sovelluksesta komennolla 7.

