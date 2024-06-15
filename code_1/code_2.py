# Dışarıdan alınan değere göre aşağıdaki mesajları ekranda gösteriniz.

x=int(input('Bir not değeri giriniz:'))

if (x>=0 and x<=50):
    print("c")
elif(x>50 and x<=80):
    print("b")
elif(x>80 and x<=100):
    print("a")
else:
    print("gecersiz")