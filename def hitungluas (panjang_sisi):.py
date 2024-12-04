# #Fugnsi hitung luas persegi
# def hitungluas  (panjang,lebar):
#     return round (panjang*lebar,2)

# panjang = float(input("input panjang sisi= "))
# lebar = float(input("input lebar sisi = "))
# print ("Luas persegi panjang = ", hitungluas(panjang,lebar))

# #fungsi menghitung volume
# def hitungvolume (p,l,t=1):
#     return round (p*l*t)
# p = float(input("input panjang sisi= "))
# l = float(input("input lebar sisi= "))
# print ("hitung volume = ", hitungvolume(p,l))
# #hitung dengan tinggi 15
# print ("hitung  volume t 15 =", hitungvolume(p,l,t=15))

#ffungsi ask
# def sortingnumber (*args):
#     return sorted (args)
# hasil = sortingnumber (5,7,100,78,14)
# print (hasil)

# #Fugnsi hitung luas persegi
def hitungluas  (panjang,lebar):
     return (panjang*lebar)

panjang = float(input("input panjang sisi= "))
lebar = float(input("input lebar sisi = "))
hasil = hitungluas (panjang,lebar)
print ("hasil hitung luas" , hasil)

# #fungsi menghitung volume
def hitungvolume (p,l,t=1):
     return (p*l*t)
p = float(input("input panjang sisi= "))
l = float(input("input lebar sisi= "))
hasil_t_fix = hitungvolume (p,l)
print ("hasil t fix" , hasil_t_fix)
#hitung dengan tinggi 15
hasil_t15 = hitungvolume(p,l,t=15)
print ("hasil t15" , hasil_t15)