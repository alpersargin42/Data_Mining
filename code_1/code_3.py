'''
#! for döngüsü

başlangıc-bitiş-artis

'''
#10 a kadar olan sayıları yazma

for i in range(1,10):
    print(i)

print("===================================================")
#? 2 şer 2 şer 10 a kadar yazma

for i in range(1,10,2):
    print(i)

print("===================================================")

#! Birden ona kadar olan sayıların toplamı
toplam = 0
for i in range(1,11):
    toplam = toplam+i
print(toplam)