# Toteutusdokumentti
## Ohjelman yleisrakenne
Ohjelma koostuu luokista `HuffmanCoding` ja `HuffmanNode`, jotka toteuttavat Huffmanin koodausta sekä luokasta `LZ77`, joka toteuttaa Lempel-Zivin algoritmia.
Ohjelmassa verrataan Huffmanin koodausta ja Lempel-Zivin algoritmia eri kokoisilla ja mahdollisesti erityyppisillä tiedostoilla.

### Huffmanin koodaus
Huffmanin koodaus perustuu Huffmanin puuhun, joka hyödyntää binääripuuta. Algoritmissa jokainen pakattavassa tiedostossa esiintyvä merkki sijoitetaan Huffmanin puun lehtiin. Merkit järjestetään siinä järjestyksessä, missä ne esiintyvät useammin. Järjestämisen jälkeen merkeille asetetaan oma binääriluku, joka tallennetaan hajautustauluun. Mitä useammin merkki esiintyy pakattavassa tiedostossa, sitä lyhyempi binääriluku asetetaan merkille. Kun jokaisella merkilla on binääriluku, tiedoston sisältö korvataan binääriluvuilla. Lopuksi pakataan uudelleen kirjoitettu tiedosto uuteen tiedostoon bitteinä. Pakatun tiedoston purkamiseen tarvitaan tiedoston pakatessa luotua hajatustaulua.

Huffmanin koodauksessa käytetään binäärihakupuuta ja kekoa. Koska binäärihakupuun muodostamiseen kuluu O(*n*log*n*) aikaa ja kekoon O(*n*), ohjelman aikavaativuus on O(*n*log*n*).

### LZ77-algoritmi
Lempel-Ziv algoritmi toimii tallentamalla tietoa sanastoon. Uudet merkit lisätään sanastoon sellaisenaan. Havaitessa toistuvia jaksoja lisätään sanastoon viittaus edelliseen jaksoon.

Kärkkäisen (2016) mukaan LZ77-algoritmi voidaan toteuttaa ajassa O(n) eli käymällä kerran pakattava tiedosto läpi.

## Saavutetut aika- ja tilavaativuudet
### Huffmanin koodaus

Aikavaativuus on O(*n*log*n*), kuten olikin tavoitteena.
Käydään läpi, missä ajassa luokan `Huffman coding` metodit suoriutuvat

`frequency_dict` - O(*n*), käy kerran tiedoston läpi
`order_nodes` - O(*n*log*n*), käy kerran kirjaston `frequency` läpi ja lisää alkion kekoon `node_heap`
`connect_nodes` - O(*n*log*n*), käy kerran keon `node_heap` läpi ja lisää alkion kekoon `node_heap`
`create_binary_codes` - O(*n*), käy kerran Huffmanin puun läpi
`encode_text` - O(*n*), käy kerran tiedoston läpi
`pad_binary_code` - O(*n*), käy kerran koodatun tiedoston läpi
`compress` - O(*n*log*n*), suorittaa kerran jokaista yllä olevaa metodia

## Suorituskyky- ja O-analyysivertailu

## Työn mahdolliset puutteet ja parannusehdotukset
- Ohjelma pystyy pakata ainoastaan tekstitiedostoja
- Ohjelma ei pysty pakkaamaan tiedostoja halutulla tavalla, jos tiedostossa käytetään laajempaa merkistöä kuin 8-bittisessä merkistössä

## Lähteet
- Kärkkäinen, Juha; Kempa, Dominik; Puglisi, Simon (2016) Lazy Lempel-Ziv Factorization Algorithms: https://dl-acm-org.libproxy.helsinki.fi/doi/abs/10.1145/2699876 (Luettu 29.10.2021)
- Wikipedia (2021) Huffman Coding: https://en.wikipedia.org/wiki/Huffman_coding (Luettu 8.10.2021)
- Wikipedia (2021) LZ77 and LZ78: https://en.wikipedia.org/wiki/LZ77_and_LZ78 (Luettu 8.10.2021)