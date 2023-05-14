## Rakenne:

Tässä kaaviossa näkyy sovelluksen pakkausrakenne. Pakkaus ui sisältää käyttöliittymän, logic sisältää sovelluslogiikan, repositories vastaa tiedon tallennuksesta tietokantaan, ja entities sisältää sisältää olio-luokkia kuten User, Item, ja List.

![pakkausrakenne](https://user-images.githubusercontent.com/101975853/235751379-a62af052-9c6d-4331-9825-a3eafc67558b.png)

## Käyttöliittymä
Sovelluksen käyttöliittymä on suhteellisen yksinkertainen tekstikäyttöliittymä, joka näyttää tältä:

![käyttöliittymä](https://github.com/irelinna/ohte/assets/101975853/f1dcbf28-1471-45c3-a298-dc333b53ea25)

Käyttöliittymä lukee käyttäjän antamia komentoja ja syötteitä, ja toimii niiden mukaisesti.

Tarkempaa tietoa käyttöliittymän toiminnasta löytyy [käyttöohjeesta](https://github.com/irelinna/ohte/blob/main/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md).

## Sovelluslogiikka

Tässä luokkakaaviossa näkyy sovelluksen logiikka, jossa käyttäjä voi luoda listoja, joissa on tavaroita (items).

[![](https://mermaid.ink/img/pako:eNptkbEKwjAQhl-l3Ch2cO3g5CLoJG4BOZpTA01Skgsipe9uEq2Y4E3Hx58vyd0EvZUEHTT9gN7vFN4camGaXHsm3QhYCWjadvvpDsrzEkh9EdjE7uzJLYFszWRaUKoQwUXJGhnU9MvGePhh3Tc3l9p0e6FNoNIOCdXe6vpKm35daFUE_7Ql6q1hMt_RzLAGTU6jknG82SeA7xRfAl1sJV0xDCxAmBTFwPb0ND107AKtIYwSmT77gO6Kg4-UpGLrju-V5c3NL-GWgIQ?type=png)](https://mermaid.live/edit#pako:eNptkbEKwjAQhl-l3Ch2cO3g5CLoJG4BOZpTA01Skgsipe9uEq2Y4E3Hx58vyd0EvZUEHTT9gN7vFN4camGaXHsm3QhYCWjadvvpDsrzEkh9EdjE7uzJLYFszWRaUKoQwUXJGhnU9MvGePhh3Tc3l9p0e6FNoNIOCdXe6vpKm35daFUE_7Ql6q1hMt_RzLAGTU6jknG82SeA7xRfAl1sJV0xDCxAmBTFwPb0ND107AKtIYwSmT77gO6Kg4-UpGLrju-V5c3NL-GWgIQ)

Sovelluksen toiminnasta vastaa luokka AppMethods. Luokasta löytyy metodit kirjautumiselle ja uloskirjautumiselle, listan luomiselle ja poistamiselle, listan etsimiselle nimen tai id:n perusteella, ja muita apumetodeja. 

AppMethods pystyy käyttämään tietokannassa olevaa tietoa repositorioiden avulla, jotka alustetaan käytettäväksi AppMethods-luokan konstruktorissa.


## Päätoiminnallisuudet:

Tässä sekvenssikaaviossa näkee miten login toimii.

![sekvenssikaavio drawio](https://user-images.githubusercontent.com/101975853/235678862-8288fdda-6730-45c9-ba7c-409b6671d6bf.png)

Kun käyttäjä on kirjautunut sisään, pystyy hän luomaan, muokkaamaan ja poistamaan listoja. 

Tässä sekvenssikaaviossa näkee mitä tapahtuu kun käyttäjä haluaa luoda listan:

[![](https://mermaid.ink/img/pako:eNptkcFqxCAQhl9lmFOXpn0ADwulvQS6UFpyE4KNsxshUavjISz77lWz29BSLzrj_J_jP2ccnCYUGOkrkR3oxahTULO0kFcXKTzs9_ddK-B5dC4SSBwCKSaYTGSJYCx0bZM3n7jmwKqZrvK2iJ-8PxCPTkcBbypGirWuL3WgrIaUX6kBO9iKV8QWF9Rr1r2Td9GwC4uAtZW-4O5-mM2Nt1sRv0V_OwrEKViINB0fT8SV1X8ulbQxd_91U1ypLtQ7bHCmMCujs5vnkpPII2UvUOSjpqNKU3ZM2ksuVYndx2IHFBwSNZi8zj-5mn9Lki4tH9YB1TldvgGW0ZTU?type=png)](https://mermaid.live/edit#pako:eNptkcFqxCAQhl9lmFOXpn0ADwulvQS6UFpyE4KNsxshUavjISz77lWz29BSLzrj_J_jP2ccnCYUGOkrkR3oxahTULO0kFcXKTzs9_ddK-B5dC4SSBwCKSaYTGSJYCx0bZM3n7jmwKqZrvK2iJ-8PxCPTkcBbypGirWuL3WgrIaUX6kBO9iKV8QWF9Rr1r2Td9GwC4uAtZW-4O5-mM2Nt1sRv0V_OwrEKViINB0fT8SV1X8ulbQxd_91U1ypLtQ7bHCmMCujs5vnkpPII2UvUOSjpqNKU3ZM2ksuVYndx2IHFBwSNZi8zj-5mn9Lki4tH9YB1TldvgGW0ZTU)

Tämän jälkeen, kun UI-luokka on saanut juuri luodun List-olion, lisätään suoraan tavarat, jotka käyttäjä syöttää. Sekvenssikaavio tästä:
[![](https://mermaid.ink/img/pako:eNptUU1rwzAM_SvCp41lf8CHQmGXHHrZ6C1QhK0sZvHHLBlWSv_77KSQrswn-enpSU-6KBMtKa2YvgsFQ28OPzP6IUB9R6b8utu9HHsNfUhFwAl5viX7ltqndCCZomUN-1EoA6GZFl4HBueZwWRCoVODAIOFhMzECwUCegKJsMms4tu_Nekr9Z1SZCcxn_W94tPsWE7O1mYxCAV5XgX-ljxOmklKDncz_Ne1uX4grJ7bWjQgf8EYM_iYaeMxVIh-nKwFqlOeskdn644vDRuUTFT1lK6hpRHLLIMawrVSsUj8OAejtORCnSrJVp-3kyg94swVJds8Hda7Lee7_gIaQJqi?type=png)](https://mermaid.live/edit#pako:eNptUU1rwzAM_SvCp41lf8CHQmGXHHrZ6C1QhK0sZvHHLBlWSv_77KSQrswn-enpSU-6KBMtKa2YvgsFQ28OPzP6IUB9R6b8utu9HHsNfUhFwAl5viX7ltqndCCZomUN-1EoA6GZFl4HBueZwWRCoVODAIOFhMzECwUCegKJsMms4tu_Nekr9Z1SZCcxn_W94tPsWE7O1mYxCAV5XgX-ljxOmklKDncz_Ne1uX4grJ7bWjQgf8EYM_iYaeMxVIh-nKwFqlOeskdn644vDRuUTFT1lK6hpRHLLIMawrVSsUj8OAejtORCnSrJVp-3kyg94swVJds8Hda7Lee7_gIaQJqi)

## Tietojen tallennus:

Sovelluksen repositorio-luokat huolehtivat tietojen tallettamisesta. UserRepository, ItemRepository, ja ListRepository-luokat tallennetaan kaikki SQLite-tietokantaan. Jokainen luokka on vastuussa tietynlaisesta tiedosta, ja jokainen luokka sekä tallentaa että hakee tietoa tietokannasta.

Konfiguraatiotiedosto .env vastaa tiedostojen nimistä. 

Tietokanta alustetaan initialize_database.py-tiedostossa. Käyttäjät tallennetaan tietokantatauluun users, listat tauluun lists, ja tavarat tauluun items.

Käyttäjät tallennetaan SQLite-tietokannan tauluun users, joka alustetaan initialize_database.py-tiedostossa.

## Ohjelmaan jääneet heikkoudet:
Käyttäjä voi tällä hetkellä löytää myös muiden käyttäjien luomia listoja jos tietää listan nimen. 

