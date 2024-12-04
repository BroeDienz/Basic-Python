pelatihan ="membangun software sederhana menggunaka python"
sesi = "operators & Control Flows"
print(pelatihan.upper())
print(sesi.upper())
print()
nama = "M Saifudin"
kegiatan = "Pertemuan Ke 2"
template ="Nama peserta : {} Praktik Mandiri : {}"
print(template.format(nama, kegiatan))
print()

#nama app ala alaa
Praktek = "pendaftaran pasien beserta triase"
print(Praktek.upper())
print()

#id pasien
name = input("nama : ")
born = input("tgl lahir d/m/y : ")
addres = input("Alamat : ")
city = input("kota : ")
id_1 = "nama pasien {} tanngal lahir {} ."
id_2 = "tinggal di {} kota {} ."

#klasifikasi usia 
age = int(input("Usia Pasien : "))
#triase suhu
trm = float(input("Suhu Tubuh : "))

print(id_1.format(name, born))
print(id_2.format(addres, city))
#run usia
if age >= 50:
  print("Lansia")
elif age >= 30:
  print("Dewasa")
elif age >= 17:
  print("Remaja")
elif age >= 6:
  print("anak anak")
else:
  print("bayi")
#run termo
if trm >= 38.5:
  print("Mati Atau Rawat Inap")
elif trm >= 37.5:
  print("Sakit Dikit Jangan Ngalem")
else:
  print("Pura pura Sakit Pengen Surat Dokter")