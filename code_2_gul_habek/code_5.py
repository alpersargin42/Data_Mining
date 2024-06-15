
'''
Bir restoranın menüsünde yer alan yemeklerin toplam fiyatını hesaplayan bir fonksiyon yazınız.

menu = {
"Hamburger":10.99,
"Pizza":8.99,
"Salata":5.99,
"Makarna":7.99,
"Çorba":3.99
}

Fonksiyon toplam fiyatı hesaplayacak.
'''

menu = {
"Hamburger":10.99,
"Pizza":8.99,
"Salata":5.99,
"Makarna":7.99,
"Çorba":3.99
}

siparis = {
    "Hamburger":3,
    "Salata":1,
    "Makarna":2
}

def hesapla(menu, siparis):
    total_price = 0
    for yemek, miktar in siparis.items():
        if yemek in menu:
            yemek_fiyat = menu[yemek]
            total_price += yemek_fiyat * miktar
    return total_price

sonuc = hesapla(menu, siparis)
print("Toplam Fiyat:", sonuc)
