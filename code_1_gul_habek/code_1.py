'''
Öğrencinin vize (%40) ve Final(%60) notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdıran python uygulamasını yazınız.

0-24---0
25-44---1
45-54---2
55-69---3
70-84---4
85-100---5
'''

vize = int(input('Vize notu:'))
final = int(input('Final notu:'))
sonuc=0
sonuc = (vize*0.4)+(final*0.6)
print("Sonuc:",sonuc)

if(sonuc>=0 and sonuc <=24):
    print("0")
elif(sonuc>=25 and sonuc <=44):
    print("1")
elif(sonuc>=44 and sonuc <=54):
    print("2")
elif(sonuc>=55 and sonuc <=69):
    print("3")
elif(sonuc>=70 and sonuc <=84):
    print("4")
elif(sonuc>=85 and sonuc <=100):
    print("5")
else:
    print("Geçersiz NOT")