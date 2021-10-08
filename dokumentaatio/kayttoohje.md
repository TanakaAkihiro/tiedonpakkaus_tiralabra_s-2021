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

