a = float(input("1.Sayı:"))
b = float(input("2.Sayı:"))
c = str(input("Hangi işlemi yapmak istiyorsunuz (bolme,carpma,cikarma,toplama):"))
if c == "bolme"or c == "carpma"or c ==  "cikarma"or c == "toplama":
    print(c,"işleminiz gerçekleştiriliyor...")
else:
    print("İşleminiz gerçekleştirilemiyor.")
if c == "bolme":
    if b != 0: #0dan farklı ise
        print(a/b)
    else:
        print("0'a bölünemez!")
elif c == "carpma":
    print(a*b)
elif c == "toplama":
    print(a+b)
elif c == "cikarma":
    print(a-b)
    
   