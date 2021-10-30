# Testausdokumentti

Ohjelma yksikkö- ja integraatiotestausta on testattu unittestilla ja järjestelmätestaus testattu manuaalisesti.

## Yksikkö- ja integraatiotestaus

* Luokkaa `HuffmanNode` testataan tiedostossa `huffman_node_test.py`
* Luokkaa `HuffmanCoding` testataan tiedostossa `huffman_coding_test.py`. Luokan testissä hyödynnetään valeluokkaa `FakeHuffmanNode`

## Testauskattavuus

![Testikattavuus](https://github.com/TanakaAkihiro/tiedonpakkaus_tiralabra_s-2021/blob/master/dokumentaatio/kuvat/testikattavuus_lopullinen.png)

## Minkälaisilla syötteillä testaus tehtiin?

[Toteutusdokumentista](https://github.com/TanakaAkihiro/tiedonpakkaus_tiralabra_s-2021/blob/master/dokumentaatio/toteutusdokumentti.md) löytyy, millä eri tiedostoilla on testattu ohjelmaa.

## Miten testit voidaan toistaa?

Testit voidaan toistaa antamalla syötteen "1" tai "2" riippuen, mitä algoritmia haluaa käyttää.

Jos ohjelman suoritus on kerran lopetettu, ohjelman voi taas suorittaa komennolla

```
poetry run invoke start
```