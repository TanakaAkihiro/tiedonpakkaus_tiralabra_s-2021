# Käyttöohje
## Ohjelman käyttnistäminen
Ennen ohjelman käynnistämistä asenna riippuvuudet komennolla
```
poetry install
```
Käynnistä ohjelma komennolla:
```
poetry run invoke start
```

## Ohjelman hyväksyviä syötteitä
Ohjelma ei varsinaisesti vastaanota mitään syötteitä. Ohjelman käyttäjä voi silti itse lisätä tekstitiedostoja pakattavaksi ja purettavaksi seuraavalla tavalla:

1. Lisää pakattava tekstitiedosto hakemistoon `files` .txt-muodossa.
2. Muokkaa tiedostossa `.env` sijaitsevan ympäristömuuttujan nimi haluamasi tiedoston nimeksi.
3. Aja sitten ohjelma tavalliseen tapaan.

## Ohjelman suorittaminen
Kun pakattava tiedosto on oikeassa hakemistossa ja ympäristömuuttujalla on oikea nimi, ohjelman voi suorittaa komennolla
```
poetry run invoke start
```

Ohjelma näyttää aluksi seuraavalta

![kuva1](https://github.com/TanakaAkihiro/tiedonpakkaus_tiralabra_s-2021/blob/master/dokumentaatio/kuvat/kaytto-ohje1.png)

Käyttäjä voi valita pakkausmetodin kahdesta vaihtoehdosta:
- antamalla syötteen "1" tiedosto pakataan (ja puretaan) Huffmanin pakkauksella

![kuva2](https://github.com/TanakaAkihiro/tiedonpakkaus_tiralabra_s-2021/blob/master/dokumentaatio/kuvat/kaytto-ohje2.png)

- antamalla syötteen "2" tiedosto pakataan (ja puretaan) LZ77-algoritmilla

![kuva3](https://github.com/TanakaAkihiro/tiedonpakkaus_tiralabra_s-2021/blob/master/dokumentaatio/kuvat/kaytto-ohje3.png)



Ohjelman voi lopettaa antamalla syötteen "3".

![kuva4](https://github.com/TanakaAkihiro/tiedonpakkaus_tiralabra_s-2021/blob/master/dokumentaatio/kuvat/kaytto-ohje4.png)
