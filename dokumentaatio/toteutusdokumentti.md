# Toteutusdokumentti
## Ohjelman yleisrakenne
Ohjelma koostuu luokista `HuffmanCoding` ja `HuffmanNode`, jotka toteuttavat Huffmanin koodausta sekä luokasta `LZ77`, joka toteuttaa Lempel-Zivin algoritmia.
Ohjelmassa verrataan Huffmanin koodausta ja Lempel-Zivin algoritmia eri kokoisilla ja mahdollisesti erityyppisillä tiedostoilla.
### Huffmanin koodaus
Huffmanin koodaus perustuu Huffmanin puuhun, joka hyödyntää binääripuuta. Algoritmissa jokainen pakattavassa tiedostossa esiintyvä merkki sijoitetaan Huffmanin puun lehtiin. Merkit järjestetään siinä järjestyksessä, missä ne esiintyvät useammin. Järjestämisen jälkeen merkeille asetetaan oma binääriluku, joka tallennetaan hajautustauluun. Mitä useammin merkki esiintyy pakattavassa tiedostossa, sitä lyhyempi binääriluku asetetaan merkille. Kun jokaisella merkilla on binääriluku, tiedoston sisältö korvataan binääriluvuilla. Lopuksi pakataan uudelleen kirjoitettu tiedosto uuteen tiedostoon bitteinä. Pakatun tiedoston purkamiseen tarvitaan tiedoston pakatessa luotua hajatustaulua.
