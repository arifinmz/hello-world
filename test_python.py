print "Hello World"

kalimat = "===aku adalah lelaki===="
print("print(kalimat)=", kalimat)
print("print(kalimat[0])=", kalimat[0])
print("print(kalimat[0:5])=", kalimat[0:5])
print("print(kalimat[4:])=", kalimat[4:])

list1 = ['pertama',1,3.0,'terakhir']
print(list1)
print(list1[0])
print(list1[0:1])

#meminta user input bilangan
#bill1 = input("Masukkan bilangan pertama:")
#bill2 = input("Masukkan bilangan kedua:")

#menjumlahkan bilangan
#jumlah = float(bill1) + float(bill2)

# menampilkan hasil
#print('Jumlah {0}+{1} adalah {2}'.format(bill1,bill2,jumlah))
#print(jumlah)

#sisi = input("Masukkan sisi persegi:")

def luaspersegi():
    sisi = input("Masukkan sisi persegi:")
    luas = sisi * sisi
    return luas

def volumepersegi(sisi):
    volume = luaspersegi(sisi) * sisi
    return volume

luaspersegi(sisi)
#volumepersegi(sisi)

print("Luas =",luas)
#print("Volume =",volume)