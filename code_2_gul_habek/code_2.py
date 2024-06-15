
#! Dictionary Tanımlama

sozluk_ornek={"sayi1":2, "sayi2":5, "sayi3":33}

print(sozluk_ornek["sayi2"])

sozluk_ornek["sayi5"] = 55

print(sozluk_ornek["sayi5"])

print(sozluk_ornek)


sozluk_ornek["sayi5"] = sozluk_ornek["sayi2"]+ sozluk_ornek["sayi3"]

print(sozluk_ornek)

print(type(sozluk_ornek))

print(sozluk_ornek.values())
print(sozluk_ornek.items())