
'''
Bir fonksiyon tanımlayarak kullanıcının girdiği 2 sayının toplamını hesaplayan bir program
fonksiyon kullanıcının girdiği sayıları almalı.
'''

def sum(sayi1,sayi2):
    toplam = sayi1+sayi2
    return toplam

sayi1=int(input('Lütfen Sayi 1 i giriniz:'))
sayi2=int(input('Lütfen Sayi 2 i giriniz:'))
print(f"Toplam {sum(sayi1,sayi2)}")