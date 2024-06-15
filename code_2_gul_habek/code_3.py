
#! List tanımlama

my_list=[1,65,89,2,15,3]

print(my_list.reverse())

print(sorted(my_list))

'''
Boş liste oluştur.
1 den 10 a kadar olan tam sayıları boş listeye ekle.
ekrana yazdır.
uzunluğunu ekrana yazdır.
listeyi tersine çevir ve tekrardan ekrana yazdır.
listeyi sıralayıp ekrana yazdır.
'''

my_list2=[]

for i in range (1,11,1):
    my_list2.append(i)

print(my_list2)

print(my_list2.__len__())

my_list2.reverse()
print(my_list2)

def reverse(liste):
    list.reverse(liste)
    return liste

print(reverse(my_list2))

my_list2.sort()
print(my_list2)
