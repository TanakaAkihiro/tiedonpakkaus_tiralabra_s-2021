# Toteutusdokumentti
## Ohjelman yleisrakenne
Ohjelma koostuu luokista `HuffmanCoding` ja `HuffmanNode`, jotka toteuttavat Huffmanin koodausta sekä luokasta `LZ77`, joka toteuttaa Lempel-Zivin algoritmia.
Ohjelmassa verrataan Huffmanin koodausta ja Lempel-Zivin algoritmia eri kokoisilla ja mahdollisesti erityyppisillä tiedostoilla.

### Huffmanin koodaus
Huffmanin koodaus perustuu Huffmanin puuhun, joka hyödyntää binääripuuta. Algoritmissa jokainen pakattavassa tiedostossa esiintyvä merkki sijoitetaan Huffmanin puun lehtiin. Merkit järjestetään siinä järjestyksessä, missä ne esiintyvät useammin. Järjestämisen jälkeen merkeille asetetaan oma binääriluku, joka tallennetaan hajautustauluun. Mitä useammin merkki esiintyy pakattavassa tiedostossa, sitä lyhyempi binääriluku asetetaan merkille. Kun jokaisella merkilla on binääriluku, tiedoston sisältö korvataan binääriluvuilla. Lopuksi pakataan uudelleen kirjoitettu tiedosto uuteen tiedostoon bitteinä. Pakatun tiedoston purkamiseen tarvitaan tiedoston pakatessa luotua hajatustaulua.

Huffmanin koodauksessa käytetään binäärihakupuuta ja kekoa. Koska binäärihakupuun muodostamiseen kuluu O(*n*log*n*) aikaa ja kekoon O(*n*), ohjelman aikavaativuus on O(*n*log*n*).

### LZ77-algoritmi


## Suorituskyky- ja O-analyysivertailu

## Työn mahdolliset puutteet ja parannusehdotukset
- Ohjelma pystyy pakata ainoastaan tekstitiedostoja
- Ohjelma ei pysty pakkaamaan tiedostoja halutulla tavalla, jos tiedostossa käytetään laajempaa merkistöä kuin 8-bittisessä merkistössä

## Lähteet
- Wikipedia (2021) Huffman Coding: https://en.wikipedia.org/wiki/Huffman_coding (Luettu 8.10.2021)
- Wikipedia (2021) LZ77 and LZ78: https://en.wikipedia.org/wiki/LZ77_and_LZ78 (Luettu 8.10.2021)