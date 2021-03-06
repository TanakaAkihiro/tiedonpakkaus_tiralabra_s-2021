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



Käydään läpi, missä ajassa luokan `Huffman coding` metodit suoriutuvat

`frequency_dict` - O(*n*), käy kerran tiedoston läpi

`order_nodes` - O(*n*log*n*), käy kerran kirjaston `frequency` läpi ja lisää alkion kekoon `node_heap`

`connect_nodes` - O(*n*log*n*), käy kerran keon `node_heap` läpi ja lisää alkion kekoon `node_heap`

`create_binary_codes` - O(*n*), käy kerran Huffmanin puun läpi

`encode_dictionary` - O(*n*), muuttaa sanakirjan merkkijonoksi ja käy kerran merkkijonon merkit läpi

`encode_text` - O(*n*), käy kerran tiedoston läpi

`pad_binary_code` - O(*n*), käy kerran koodatun tiedoston läpi

`compress` - O(*n*log*n*), suorittaa kerran jokaista yllä olevaa metodia

`decode_byte_code` - O(*n*), käy kerran pakatun tiedoston läpi

`decode_text` - O(*n*), käy kerran annetun binäärilukujen merkkijonon läpi

`decompress` - O(*n*), suorittaa kerran metodeja `decode_byte_code` ja `decode_text`

Aikavaativuus on siis O(*n*log*n*), kuten olikin tavoitteena.

Tilavaativuus on O(*n* + *k*), missä *n* on tiedoston tekstin merkkien määrä ja *k* Huffmanin puun solmujen määrä.

### LZ77-algoritmi



Käydään läpi, missä ajassa luokan `LZ77` metodit suoriutuvat

`search_best_match` - O(12*n*) = O(*n*), käy 12 kertaa osajonojen *n* läpi

`encode_text` - O(*n*²), käy kerran tiedoston läpi, jonka aikana suorittaa metodin `search_best_match`

`pad_binary_code` - O(*n*), käy kerran koodatun tiedoston läpi

`compress` - O(*n*²), suorittaa kerran jokaista yllä olevaa metodia

`decode_byte_code` - O(*n*), käy kerran pakatun tiedoston läpi



Aikavaativuus on siis O(*n*²).



## Suorituskyky- ja O-analyysivertailu
Pakkausalgoritmeja suoritettiin viidellä eri tiedostolla:

1. Lorem ipsum
2. Yksi pitkä merkkijono, joka koostuu numeroista 0-9
3. Yksi pitkä merkkijono, joka koostuu merkeistä '0' ja '1'
4. Yksi pitkä merkkijono, joka koostuu pelkästään merkistä 'a'
5. Seitsemän veljestä

Ensimmäinen kuva esittää tiedostojen alkuperäisen koon sekä niiden koon Huffmanin koodauksen tai LZ77-pakkauksen jälkeen.

![kuva1](https://github.com/TanakaAkihiro/tiedonpakkaus_tiralabra_s-2021/blob/master/dokumentaatio/kuvat/toteutus1.png)

Toinen kuva esittää pakattavien tiedostojen alkuperäisen koon ja Huffmanin koodauksella/LZ77 algoritmilla pakatun tiedoston koon suhdetta

![kuva2](https://github.com/TanakaAkihiro/tiedonpakkaus_tiralabra_s-2021/blob/master/dokumentaatio/kuvat/toteutus2.png)

Huffmanin koodaus toimii tasaisesti hyvin. Mitä vähemmän erilaisia merkkejä esiintyy tiedostossa, sitä tehokkaammin Huffmanin koodaus voi pakata tiedoston.

LZ77 algoritmi toimii tehokkaammin kuin Huffmanin koodaus, kun tiedostossa esiintyy paljon toistuvia jaksoja. Toisaalta, jos toistuvia jaksoja esiintyy harvoin, pakkaussuhde on hyvin korkea (jopa yli 100%).


Seuraava taulu esittää pakkaamisen kestoa millisekunneissa (ms)

|           | Huffmanin koodaus |      LZ77      |
|-----------|:-----------------:|---------------:|
|   Text1   |         3.06      |      134.60    |
|   Text2   |       130.75      |    36326.69    |
|   Text3   |       121.76      |    23117.36    |
|   Text4   |       205.79      |    36913.22    |
|   Text5   |       232.77      |   348690.33    |

Seuraava taulu esittää purkamisen kestoa millisekunneissa (ms)

|           | Huffmanin koodaus |      LZ77      |
|-----------|:-----------------:|---------------:|
|   Text1   |         3.80      |        0.57    |
|   Text2   |       162.42      |     2881.49    |
|   Text3   |       180.87      |     2002.49    |
|   Text4   |       235.25      |     3725.39    |
|   Text5   |       643.18      |   118788.64    |

Taulusta tulee selkeästi ilmi, että Huffmanin koodaus toimii ajalla tehokkaammin kuin LZ77 algoritmi. Tämä johtuukin siitä, että Huffmanin koodauksen aikavaativuus on O(*n*log*n*) ja LZ77 algoritmin O(*n*²).

Toinen tärkeä havainto, joka nähdään taulusta on se, että Huffmanin koodauksella pakkaamiseen kestää vähemmän aikaa kuin purkamiseen ja LZ77 algoritmilla toisin päin.


## Työn mahdolliset puutteet ja parannusehdotukset
- Ohjelma pystyy pakata ainoastaan tekstitiedostoja
- Ohjelma ei pysty pakkaamaan tiedostoja halutulla tavalla, jos tiedostossa käytetään laajempaa merkistöä kuin 8-bittisessä merkistössä

## Lähteet
- Kärkkäinen, Juha; Kempa, Dominik; Puglisi, Simon (2016) Lazy Lempel-Ziv Factorization Algorithms: https://dl-acm-org.libproxy.helsinki.fi/doi/abs/10.1145/2699876 (Luettu 29.10.2021)
- Wikipedia (2021) Huffman Coding: https://en.wikipedia.org/wiki/Huffman_coding (Luettu 8.10.2021)
- Wikipedia (2021) LZ77 and LZ78: https://en.wikipedia.org/wiki/LZ77_and_LZ78 (Luettu 8.10.2021)
