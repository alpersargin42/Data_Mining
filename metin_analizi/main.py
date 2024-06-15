import pandas as pd
import nltk
from nltk.corpus import stopwords



metin = """
A Scandal in Bohemia! 01
The Red-headed League beryl,2 studies
A Case, of Identity 33
The Boscombe Valley Mystery4 League studies
The Five Orange Pips1 League beryl sandy
The Man with? the Twisted Lip studying
The Adventure of the Blue Carbuncle
The Adventure of the Speckled Band studying
The Adventure of the Engineer's Thumb Mystery
The Adventure of the Noble Bachelor League
The Adventure of the Beryl Coronet Mystery sandy
The Adventure of the Copper Beec"""
print(metin)
list_metin=metin.split("\n")
seri_metin=pd.Series(list_metin)
print(seri_metin)

seri_metin=seri_metin[1:len(seri_metin)]
print(seri_metin)

#normalization
seri_metin=seri_metin.apply(lambda x:" ".join(kelime.lower() for kelime in x.split()))
print(seri_metin)

#noktalama işaretleri ve sayıların silinmesi /işaretler silindi
seri_metin=seri_metin.str.replace("[^\w\s]", "",regex=True)
print(seri_metin)
#sayılar silindi
seri_metin=seri_metin.str.replace("[\d]","",regex=True)
print(seri_metin)

print(nltk.download("stopwords"))

stopwordsList=stopwords.words("english")
print(stopwordsList)

seri_metin=seri_metin.apply(
    lambda x:" " .join(kelime for kelime in x.split() if kelime not in stopwordsList)
    )
print(seri_metin)

#az geçen 3 kelimeyi çıkartıyoruz
words=pd.Series(" ".join(seri_metin).split())
words_count=words.value_counts()
print(words)
print(words_count)
print("*********")
enSonUcKelime=words_count[-3:]
print(enSonUcKelime)

seri_metin=seri_metin.apply(
    lambda x:" " .join(kelime for kelime in x.split() if kelime not in enSonUcKelime)
    )
print(seri_metin)