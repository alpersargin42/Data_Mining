import pandas as pd
import nltk
from nltk.corpus import stopwords


metin= """Bugün hava çok güzel, yürüyüşe çıkabilirim. Yarın, 3 sınavım var. Şimdi çıkmazsam; bir sonraki treni kaçıracağım. Marketten alınacaklar: çay, kahve, kalem. . #."""
print(metin)
list_metin=metin.split(".")
seri_metin=pd.Series(list_metin)
print(seri_metin)

seri_metin = seri_metin[:-3]
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

stopwordsList=stopwords.words("english")

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