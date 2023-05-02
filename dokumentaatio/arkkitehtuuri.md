## Rakenne:

Tässä kaaviossa näkyy sovelluksen pakkausrakenne. Pakkaus ui sisältää käyttöliittymän, logic sisältää sovelluslogiikan, repositories vastaa tiedon tallennuksesta tietokantaan, ja entities sisältää sisältää olio-luokkia kuten User, Item, ja List.

![pakkausrakenne](https://user-images.githubusercontent.com/101975853/235751379-a62af052-9c6d-4331-9825-a3eafc67558b.png)


## Sovelluslogiikka

Tässä luokkakaaviossa näkyy sovelluksen logiikka, jossa käyttäjä voi luoda listoja, joissa on tavaroita (items).

[![](https://mermaid.ink/img/pako:eNptkbEKAjEMhl_lyCje4HqDk4ugk7gVJLRRC9dW2hSR497dtt7JVcwUPn6-tMkA0imCDhrZYwg7jTePRtim1J7JNAJWApq23U7dQQeeA7mvApvUnQP5OVCshQwzyhUTsGhoyR4p-XRezWysHXlU5cjgotUS9Rn9evOsRe5Hm79YaXUC_7Q1ks4y2e8eRliDIW9Qq7TL4hPAd0ovgS61iq4YexYgbI5iZHd6WQkd-0hriA-FTNPyobtiHxIlpdn54-c-5UzjGztCe48?type=png)](https://mermaid.live/edit#pako:eNptkbEKAjEMhl_lyCje4HqDk4ugk7gVJLRRC9dW2hSR497dtt7JVcwUPn6-tMkA0imCDhrZYwg7jTePRtim1J7JNAJWApq23U7dQQeeA7mvApvUnQP5OVCshQwzyhUTsGhoyR4p-XRezWysHXlU5cjgotUS9Rn9evOsRe5Hm79YaXUC_7Q1ks4y2e8eRliDIW9Qq7TL4hPAd0ovgS61iq4YexYgbI5iZHd6WQkd-0hriA-FTNPyobtiHxIlpdn54-c-5UzjGztCe48)

Sovelluksen toiminnasta vastaa luokka AppMethods. Luokasta löytyy metodit kirjautumiselle ja uloskirjautumiselle, listan luomiselle ja poistamiselle, listan etsimiselle nimen tai id:n perusteella, ja muita apumetodeja. 

AppMethods pystyy käyttämään tietokannassa olevaa tietoa repositorioiden avulla, jotka alustetaan käytettäväksi AppMethods-luokan konstruktorissa.


## Päätoiminnallisuudet:

Tässä sekvenssikaaviossa näkee miten login toimii.

![sekvenssikaavio drawio](https://user-images.githubusercontent.com/101975853/235678862-8288fdda-6730-45c9-ba7c-409b6671d6bf.png)

