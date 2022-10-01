isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
print(isimler.append('Cenk'))
# 2-  "Sena" değerini listenin başına ekleyiniz.
print(isimler.insert(0, 'Sena'))
# 3-  "Yiğit" ismini listeden siliniz.
print(isimler.pop(1))
# 4-  "Yiğit" isminin indeksi nedir ?
index  = isimler.index('Yiğit')
print(isimler.pop(index))
# 5-  "Beril" listenin bir elemanı mıdır ?
cozum5 = isimler.index('Beril')
print(cozum5)
# 6-  Liste elemanlarını ters çevirin.
print(isimler.reverse())
# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
print(isimler.sort())
# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.
print(yaslar.sort())
# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
isimler += ["IPhone X", "IPhone XR"]
print(isimler)
# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
min = min(yaslar)
max = max(yaslar)
print(min, max)
# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
print(yaslar.count(1998))
# 12- yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear()
print(yaslar)
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
print(markalar)