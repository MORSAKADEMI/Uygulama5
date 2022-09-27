isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
isimler.append("Cenk")
print(isimler)

# 2-  "Sena" değerini listenin başına ekleyiniz.
isimler.insert(0,"Sena")
print(isimler)

# 3-  "Yiğit" ismini listeden siliniz.
isimler.remove("Yiğit")
print(isimler)

# 4-  "Yiğit" isminin indeksi nedir ?
isimler.append("Yiğit")
print(isimler.index("Yiğit"))

# 5-  "Beril" listenin bir elemanı mıdır ?
if "Beril" in isimler:
    print("true")
else:
    print("false")
    
# 6-  Liste elemanlarını ters çevirin.
isimler.pop()
isimler.reverse()
print(isimler)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
isimler.sort()
print(isimler)

# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.
yaslar.sort()
yaslar.reverse()
print(yaslar)

# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
s = ["IPhone X", "IPhone XR"]
print(s)

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
print(max(yaslar),min(yaslar))


# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
print(yaslar.count(1998))

# 12- yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear()
print(yaslar)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
bilgi1, bilgi2, bilgi3 = input("marka giriniz:"),input("ikinci markayı giriniz:"),input("üçüncü markayı giriniz:")
liste = [bilgi1, bilgi2, bilgi3]
print(liste)
